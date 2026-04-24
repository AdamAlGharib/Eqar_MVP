# Supabase Setup

The first migration creates tenant-scoped tables, basic row-level security, and a `pgvector` document chunk table for retrieval.

Before production:
- Confirm the embedding dimension matches the configured embedding model.
- Add storage buckets for uploaded documents and generated exports.
- Review all RLS policies against the final API access pattern.
- Add malware scanning before public uploads.
