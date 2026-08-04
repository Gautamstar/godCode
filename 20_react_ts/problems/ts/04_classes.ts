/**
 * PROBLEM : Classes, Access Modifiers & Inheritance
 * TOPIC   : TypeScript basics
 * LEVEL   : Easy
 *
 * TypeScript adds `public`, `private`, `protected`, and `readonly` to classes.
 * Putting a modifier on a constructor parameter declares AND assigns the field
 * in one step, which is the shorthand assessments love.
 *
 * Hint (only peek if you are stuck):
 *   Shorthand field:  constructor(protected name: string) {}
 *   Call the parent:  super(name)
 *   Getter:           get label(): string { return ...; }
 *   Static counter:   static count = 0;  then Animal.count++
 *
 * HOW TO RUN:  npx vitest run problems/ts/04_classes
 */

export class Animal {
  /**
   * `name` must be readable by subclasses but NOT from outside the class.
   * Declare it with the constructor-parameter shorthand.
   *
   * Also keep a static `count` of how many Animals have been constructed
   * (subclasses included), starting at 0.
   */
  // YOUR CODE HERE (static count, constructor)

  /**
   * Returns "<name> makes a sound".
   */
  speak(): string {
    // YOUR CODE HERE
    throw new Error("not implemented");
  }

  /**
   * A getter (called as `animal.label`, no parentheses) returning
   * "Animal: <name>".
   */
  // YOUR CODE HERE (get label)
}

export class Dog extends Animal {
  /**
   * A Dog is built from a name and a breed. Pass the name up to Animal.
   */
  // YOUR CODE HERE (constructor taking name and public breed)

  /**
   * Override: returns "<name> barks".
   */
  speak(): string {
    // YOUR CODE HERE
    throw new Error("not implemented");
  }

  /**
   * Returns "<name> is a <breed>".
   */
  describe(): string {
    // YOUR CODE HERE
    throw new Error("not implemented");
  }
}
