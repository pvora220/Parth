const nodes = [
  { id: "target", label: "target" },
  { id: "github", label: "github" },
];

const edges = [{ source: "target", target: "github" }];

export default function Graph() {
  return (
    <section>
      <h2>Graph Preview</h2>
      <pre>{JSON.stringify({ nodes, edges }, null, 2)}</pre>
    </section>
  );
}
