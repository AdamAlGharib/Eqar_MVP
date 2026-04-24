export type UUID = string;

export type AgentRole = "owner" | "agent" | "assistant_viewer";

export type AnswerMode = "draft" | "export";

export type CountryCode = "CA" | string;

export type ProvinceCode = "ON" | string;

export type ProcessingStatus =
  | "queued"
  | "processing"
  | "ready"
  | "failed"
  | "deleted";

export interface WorkspaceSummary {
  id: UUID;
  name: string;
  role: AgentRole;
}

export interface ProjectSummary {
  id: UUID;
  workspaceId: UUID;
  name: string;
  countryCode: CountryCode;
  provinceCode?: ProvinceCode;
}

export interface ChatMessage {
  id: UUID;
  conversationId: UUID;
  role: "user" | "assistant" | "system" | "tool";
  content: string;
  createdAt: string;
  metadata?: Record<string, unknown>;
}

export interface ToolProvenance {
  toolName: string;
  toolVersion: string;
  countryCode?: CountryCode;
  provinceCode?: ProvinceCode;
  assumptions: string[];
  sources: SourceReference[];
}

export interface SourceReference {
  label: string;
  url?: string;
  documentId?: UUID;
  pageNumber?: number;
}

export interface AnalysisRunSummary {
  id: UUID;
  projectId: UUID;
  kind: "listing_prep" | "property_analysis" | "buyer_scenario" | "client_message";
  title: string;
  status: "queued" | "running" | "completed" | "failed";
  createdAt: string;
}
