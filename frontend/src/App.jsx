import { useMemo, useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

export default function App() {
  const [a, setA] = useState("0");
  const [b, setB] = useState("0");
  const [op, setOp] = useState("add");

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const endpoint = useMemo(() => {
    // maps operation to your FastAPI routes
    return `${API_BASE}/api/${op}`;
  }, [op]);

  async function calculate() {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const url = new URL(endpoint);
      url.searchParams.set("a", a);
      url.searchParams.set("b", b);

      const res = await fetch(url.toString(), {
        method: "GET",
        headers: { Accept: "application/json" },
      });

      const data = await res.json().catch(() => null);

      if (!res.ok) {
        // FastAPI error body is usually { detail: "..." }
        const msg =
          (data && (data.detail || data.message)) ||
          `Request failed with status ${res.status}`;
        throw new Error(msg);
      }

      setResult(data);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", padding: 24, maxWidth: 520 }}>
      <h1 style={{ marginTop: 0 }}>Calculator UI</h1>

      <div style={{ display: "grid", gap: 12 }}>
        <label style={{ display: "grid", gap: 6 }}>
          A
          <input
            type="number"
            value={a}
            onChange={(e) => setA(e.target.value)}
            style={{ padding: 10, borderRadius: 8, border: "1px solid #ccc" }}
          />
        </label>

        <label style={{ display: "grid", gap: 6 }}>
          B
          <input
            type="number"
            value={b}
            onChange={(e) => setB(e.target.value)}
            style={{ padding: 10, borderRadius: 8, border: "1px solid #ccc" }}
          />
        </label>

        <label style={{ display: "grid", gap: 6 }}>
          Operation
          <select
            value={op}
            onChange={(e) => setOp(e.target.value)}
            style={{ padding: 10, borderRadius: 8, border: "1px solid #ccc" }}
          >
            <option value="add">add</option>
            <option value="subtract">subtract</option>
            <option value="multiply">multiply</option>
            <option value="divide">divide</option>
          </select>
        </label>

        <button
          onClick={calculate}
          disabled={loading}
          style={{
            padding: 12,
            borderRadius: 10,
            border: "none",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          {loading ? "Calculating..." : "Calculate"}
        </button>

        <div style={{ marginTop: 12 }}>
          <h3 style={{ marginBottom: 8 }}>Response</h3>

          {error && (
            <div
              style={{
                padding: 12,
                borderRadius: 10,
                border: "1px solid #f5c2c7",
                background: "#f8d7da",
              }}
            >
              <b>Error:</b> {error}
            </div>
          )}

          {result && (
            <pre
              style={{
                padding: 12,
                borderRadius: 10,
                border: "1px solid #ddd",
                background: "#fafafa",
                overflowX: "auto",
              }}
            >
              {JSON.stringify(result, null, 2)}
            </pre>
          )}

          {!error && !result && (
            <div style={{ color: "#666" }}>No result yet. Enter numbers and calculate.</div>
          )}
        </div>
      </div>
    </div>
  );
}
