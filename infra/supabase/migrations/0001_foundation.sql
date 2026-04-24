create extension if not exists "pgcrypto";
create extension if not exists "vector";

create table if not exists public.workspaces (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  slug text not null unique,
  subscription_status text not null default 'trial',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.workspace_members (
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('owner', 'agent', 'assistant_viewer')),
  created_at timestamptz not null default now(),
  primary key (workspace_id, user_id)
);

create table if not exists public.projects (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  name text not null,
  country_code text not null default 'CA',
  province_code text,
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.conversations (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  title text not null default 'Untitled conversation',
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid not null references public.conversations(id) on delete cascade,
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  role text not null check (role in ('user', 'assistant', 'system', 'tool')),
  content text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists public.documents (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  uploaded_by uuid references auth.users(id) on delete set null,
  storage_path text not null,
  filename text not null,
  content_type text not null,
  byte_size bigint not null check (byte_size >= 0),
  status text not null default 'queued' check (status in ('queued', 'processing', 'ready', 'failed', 'deleted')),
  checksum text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.document_chunks (
  id uuid primary key default gen_random_uuid(),
  document_id uuid not null references public.documents(id) on delete cascade,
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  chunk_index integer not null check (chunk_index >= 0),
  content text not null,
  content_hash text not null,
  page_number integer,
  source_locator jsonb not null default '{}'::jsonb,
  embedding vector(1536),
  created_at timestamptz not null default now(),
  unique (document_id, chunk_index)
);

create table if not exists public.analysis_runs (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  conversation_id uuid references public.conversations(id) on delete set null,
  kind text not null check (kind in ('listing_prep', 'property_analysis', 'buyer_scenario', 'client_message')),
  title text not null,
  status text not null default 'queued' check (status in ('queued', 'running', 'completed', 'failed')),
  inputs jsonb not null default '{}'::jsonb,
  outputs jsonb not null default '{}'::jsonb,
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.tool_runs (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  conversation_id uuid references public.conversations(id) on delete set null,
  analysis_run_id uuid references public.analysis_runs(id) on delete set null,
  tool_name text not null,
  tool_version text not null,
  country_code text,
  province_code text,
  inputs jsonb not null default '{}'::jsonb,
  outputs jsonb not null default '{}'::jsonb,
  provenance jsonb not null default '{}'::jsonb,
  latency_ms integer,
  created_at timestamptz not null default now()
);

create table if not exists public.country_packs (
  id uuid primary key default gen_random_uuid(),
  country_code text not null,
  province_code text,
  version text not null,
  config jsonb not null default '{}'::jsonb,
  effective_from date,
  created_at timestamptz not null default now(),
  unique (country_code, province_code, version)
);

create table if not exists public.audit_logs (
  id uuid primary key default gen_random_uuid(),
  workspace_id uuid not null references public.workspaces(id) on delete cascade,
  actor_user_id uuid references auth.users(id) on delete set null,
  action text not null,
  target_type text,
  target_id uuid,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_workspace_members_user on public.workspace_members(user_id);
create index if not exists idx_projects_workspace on public.projects(workspace_id);
create index if not exists idx_conversations_workspace on public.conversations(workspace_id);
create index if not exists idx_messages_conversation on public.messages(conversation_id, created_at);
create index if not exists idx_documents_workspace on public.documents(workspace_id, status);
create index if not exists idx_document_chunks_workspace on public.document_chunks(workspace_id, document_id);
create index if not exists idx_analysis_runs_workspace on public.analysis_runs(workspace_id, status);
create index if not exists idx_tool_runs_workspace on public.tool_runs(workspace_id, created_at);
create index if not exists idx_audit_logs_workspace on public.audit_logs(workspace_id, created_at);
create index if not exists idx_document_chunks_embedding on public.document_chunks using ivfflat (embedding vector_cosine_ops) with (lists = 100);

create or replace function public.is_workspace_member(target_workspace_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1
    from public.workspace_members wm
    where wm.workspace_id = target_workspace_id
      and wm.user_id = auth.uid()
  );
$$;

alter table public.workspaces enable row level security;
alter table public.workspace_members enable row level security;
alter table public.projects enable row level security;
alter table public.conversations enable row level security;
alter table public.messages enable row level security;
alter table public.documents enable row level security;
alter table public.document_chunks enable row level security;
alter table public.analysis_runs enable row level security;
alter table public.tool_runs enable row level security;
alter table public.country_packs enable row level security;
alter table public.audit_logs enable row level security;

create policy "members can read their workspaces"
  on public.workspaces for select
  using (public.is_workspace_member(id));

create policy "members can read workspace memberships"
  on public.workspace_members for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read projects"
  on public.projects for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read conversations"
  on public.conversations for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read messages"
  on public.messages for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read documents"
  on public.documents for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read document chunks"
  on public.document_chunks for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read analysis runs"
  on public.analysis_runs for select
  using (public.is_workspace_member(workspace_id));

create policy "members can read tool runs"
  on public.tool_runs for select
  using (public.is_workspace_member(workspace_id));

create policy "authenticated users can read country packs"
  on public.country_packs for select
  to authenticated
  using (true);

create policy "members can read audit logs"
  on public.audit_logs for select
  using (public.is_workspace_member(workspace_id));
