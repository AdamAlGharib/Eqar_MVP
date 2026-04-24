import styles from "./dashboard.module.css";

const documents = [
  {
    title: "123 Queen St W disclosure",
    detail: "Parsed 14 min ago",
    status: "Ready",
    tone: "Success"
  },
  {
    title: "Martins offer package",
    detail: "Missing buyer initials on schedule B",
    status: "Action",
    tone: "Warning"
  },
  {
    title: "Oakville condo status cert",
    detail: "Awaiting upload from client",
    status: "Waiting",
    tone: "Neutral"
  }
] as const;

const checklist = ["Identity confirmed", "Consent captured", "Storage policy applied"];

export function DocumentStatusPanel() {
  return (
    <section className={styles.panel}>
      <div className={styles.panelHeader}>
        <h2>Documents</h2>
        <button className={styles.ghostButton} type="button">
          Upload
        </button>
      </div>

      <div className={styles.tableWrap}>
        <table className={styles.documentTable}>
          <thead>
            <tr>
              <th>Name</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {documents.map((document) => (
              <tr key={document.title}>
                <td>
                  <strong>{document.title}</strong>
                  <p>{document.detail}</p>
                </td>
                <td>{document.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <ul className={styles.checklist} aria-label="Compliance checklist">
        {checklist.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}
