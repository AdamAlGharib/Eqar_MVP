import Link from "next/link";

import { ChatPanel } from "./ChatPanel";
import { DocumentStatusPanel } from "./DocumentStatusPanel";
import { WorkflowCards } from "./WorkflowCards";
import styles from "./dashboard.module.css";

type DashboardShellProps = {
  missingEnv: string[];
};

const navItems = [
  { label: "Dashboard", active: true },
  { label: "Clients", active: false },
  { label: "Documents", active: false },
  { label: "Analyses", active: false },
  { label: "Settings", active: false }
];

export function DashboardShell({ missingEnv }: DashboardShellProps) {
  const envReady = missingEnv.length === 0;

  return (
    <div className={styles.dashboard}>
      <aside className={styles.sidebar} aria-label="Workspace navigation">
        <Link className={styles.brand} href="/" aria-label="Eqar dashboard home">
          Eqar
        </Link>

        <nav className={styles.navList}>
          {navItems.map((item) => (
            <Link
              aria-current={item.active ? "page" : undefined}
              className={`${styles.navItem} ${item.active ? styles.navItemActive : ""}`}
              href="/"
              key={item.label}
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>

      <main className={styles.main}>
        <header className={styles.topbar}>
          <h1>Dashboard</h1>

          <div className={styles.topbarActions}>
            <div className={styles.agentBadge} aria-label="Signed in agent">
              Avery Chen
            </div>
            <button className={styles.primaryButton} type="button">
              New analysis
            </button>
          </div>
        </header>

        {!envReady ? (
          <section className={styles.envNotice} aria-label="Local setup status">
            <strong>Local setup needs configuration</strong>
            <p>{missingEnv.join(", ")}</p>
          </section>
        ) : null}

        <div className={styles.workArea}>
          <section className={styles.primaryColumn} aria-label="Priority workflows">
            <WorkflowCards />
          </section>

          <section className={styles.secondaryColumn} aria-label="Co-pilot and documents">
            <ChatPanel />
            <DocumentStatusPanel />
          </section>
        </div>
      </main>
    </div>
  );
}
