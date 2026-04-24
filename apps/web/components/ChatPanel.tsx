import styles from "./dashboard.module.css";

const messages = [
  {
    author: "Avery",
    text: "Summarize the newest conditional sale clauses for the Martins file."
  },
  {
    author: "Eqar",
    text: "I found three conditions to review: financing, inspection, and status certificate timing."
  },
  {
    author: "Eqar",
    text: "Suggested next step: send a concise client update and flag the inspection window."
  }
];

export function ChatPanel() {
  return (
    <section className={styles.panel}>
      <div className={styles.panelHeader}>
        <h2>Chat</h2>
      </div>

      <div className={styles.chatLog} aria-label="Recent co-pilot messages">
        {messages.map((message, index) => (
          <div
            className={`${styles.message} ${
              message.author === "Avery" ? styles.messageUser : styles.messageAssistant
            }`}
            key={`${message.author}-${index}`}
          >
            <span>{message.author}</span>
            <p>{message.text}</p>
          </div>
        ))}
      </div>

      <form className={styles.chatComposer}>
        <label htmlFor="copilot-message">
          Message Eqar
        </label>
        <div className={styles.composerRow}>
          <input
            id="copilot-message"
            name="message"
            placeholder="Ask about a client, property, or document"
            type="text"
          />
          <button className={styles.sendButton} type="button">
            Send
          </button>
        </div>
      </form>
    </section>
  );
}
