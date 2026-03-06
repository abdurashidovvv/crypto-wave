import { ALGORITHMS } from "../constants/algorithms";

export default function AlgorithmTabs({ active, onChange }) {
  return (
    <div className="algorithm-tabs">
      {ALGORITHMS.map((a) => (
        <button
          key={a.id}
          className={`tab ${active === a.id ? "active" : ""}`}
          onClick={() => onChange(a.id)}
        >
          {a.label}
        </button>
      ))}
    </div>
  );
}