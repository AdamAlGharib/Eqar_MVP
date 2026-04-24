import { DashboardShell } from "@/components/DashboardShell";
import { missingPublicEnv } from "@/lib/env";

export default function Home() {
  return <DashboardShell missingEnv={missingPublicEnv} />;
}
