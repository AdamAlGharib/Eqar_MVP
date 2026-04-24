export const publicEnv = {
  appEnv: process.env.NEXT_PUBLIC_APP_ENV ?? "local",
  apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL ?? "",
  supabaseUrl: process.env.NEXT_PUBLIC_SUPABASE_URL ?? "",
  supabaseAnonKey: process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ?? ""
} as const;

const requiredPublicEnv = {
  NEXT_PUBLIC_API_BASE_URL: publicEnv.apiBaseUrl,
  NEXT_PUBLIC_SUPABASE_URL: publicEnv.supabaseUrl,
  NEXT_PUBLIC_SUPABASE_ANON_KEY: publicEnv.supabaseAnonKey
} as const;

export const missingPublicEnv = Object.entries(requiredPublicEnv)
  .filter(([, value]) => value.length === 0)
  .map(([key]) => key);
