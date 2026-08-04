export interface User {
  id: number;
  name: string;
  email?: string; // the ? makes the property optional
}

export function formatUser(u: User): string {
  // u.email is `string | undefined`, so TypeScript forces you to handle the
  // missing case. That is the entire value of marking it optional.
  return u.email ? `${u.name} <${u.email}>` : `${u.name} (no email)`;
}

// An index signature says "any string key, values are numbers". Use it when
// the key names are data, not part of the schema.
export interface Scores {
  [subject: string]: number;
}

export function bestSubject(scores: Scores): string {
  let best = "";
  for (const subject of Object.keys(scores)) {
    // strict > keeps the FIRST on a tie, since a later equal score never wins
    if (best === "" || scores[subject] > scores[best]) best = subject;
  }
  return best;
}

export function parseUser(json: string): User {
  // JSON.parse returns `any`. The assertion tells the compiler what shape to
  // expect. It is a promise you are making, not a runtime check, so only use
  // it when you actually know the shape.
  return JSON.parse(json) as User;
}
