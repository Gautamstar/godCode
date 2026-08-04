export class Animal {
  static count = 0;

  // The `protected` modifier on a constructor parameter declares the field,
  // assigns it, and sets visibility, all in one line. Without a modifier it
  // would just be a plain argument that vanishes after the constructor.
  // protected = readable by this class and subclasses, not from outside.
  constructor(protected name: string) {
    Animal.count++;
  }

  speak(): string {
    return `${this.name} makes a sound`;
  }

  // A getter is called without parentheses: animal.label
  get label(): string {
    return `Animal: ${this.name}`;
  }
}

export class Dog extends Animal {
  // `public breed` declares the field here; `name` is passed straight up to
  // the parent, which owns it.
  constructor(name: string, public breed: string) {
    super(name); // must come before any use of `this`
  }

  // Same signature as the parent, different body. The subclass version wins.
  speak(): string {
    return `${this.name} barks`;
  }

  describe(): string {
    // this.name works because Animal declared it `protected`, not `private`.
    return `${this.name} is a ${this.breed}`;
  }
}
