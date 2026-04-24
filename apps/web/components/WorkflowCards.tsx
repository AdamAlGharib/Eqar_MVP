import styles from "./dashboard.module.css";

const workflows = [
  {
    client: "M. Patel",
    file: "Riverdale semi",
    task: "CMA refresh",
    owner: "Avery",
    due: "Today",
    status: "In review",
    next: "Reconcile new sold comps"
  },
  {
    client: "M. Patel",
    file: "Buyer scenario",
    task: "Carrying cost",
    owner: "Avery",
    due: "Today",
    status: "Needs input",
    next: "Confirm down payment"
  },
  {
    client: "The Martins",
    file: "Offer package",
    task: "Offer review",
    owner: "Avery",
    due: "Tomorrow",
    status: "Open",
    next: "Check financing condition"
  },
  {
    client: "Chen estate",
    file: "Listing launch",
    task: "Seller prep",
    owner: "Avery",
    due: "Apr 28",
    status: "Open",
    next: "Draft showing notes"
  }
];

export function WorkflowCards() {
  return (
    <>
      <div className={styles.sectionHeader}>
        <h2>Work queue</h2>
        <button className={styles.ghostButton} type="button">
          Add task
        </button>
      </div>

      <div className={styles.tableWrap}>
        <table className={styles.workTable}>
          <thead>
            <tr>
              <th>Client</th>
              <th>File</th>
              <th>Task</th>
              <th>Status</th>
              <th>Due</th>
              <th>Next action</th>
            </tr>
          </thead>
          <tbody>
            {workflows.map((workflow) => (
              <tr key={`${workflow.client}-${workflow.task}`}>
                <td>{workflow.client}</td>
                <td>{workflow.file}</td>
                <td>{workflow.task}</td>
                <td>{workflow.status}</td>
                <td>{workflow.due}</td>
                <td>{workflow.next}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
