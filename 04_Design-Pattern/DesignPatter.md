Here are the **most important Object-Oriented Design (OOD) concepts** that are commonly asked and used in system design interviews (like Parking Lot, Elevator System, ATM, etc.):

---

### 🔑 **Core OOD Concepts**

1. **Abstraction**

   * Hides complex implementation details.
   * Focuses on *what* an object does, not *how* it does it.

2. **Encapsulation**

   * Bundles data and methods together.
   * Restricts direct access to internal state (use getters/setters).

3. **Inheritance**

   * Enables code reuse.
   * Allows child classes to inherit from parent (e.g., `Car` → `Vehicle`).

4. **Polymorphism**

   * Same interface, different behavior.
   * Example: `park()` behaves differently for `Bike` vs `Truck`.

---

### 📐 **SOLID Principles** (Very important in interviews)

1. **S** – Single Responsibility Principle
   A class should have only one reason to change.

2. **O** – Open/Closed Principle
   Open for extension, closed for modification.

3. **L** – Liskov Substitution Principle
   Subclasses should be replaceable for parent classes.

4. **I** – Interface Segregation Principle
   Prefer small, specific interfaces over large general ones.

5. **D** – Dependency Inversion Principle
   Depend on abstractions, not concrete implementations.

---

### 🧰 **Design Patterns** (Commonly used in LLD)

* **Singleton** – One global instance (e.g. ParkingLot, DB connection)
* **Strategy** – Replaceable algorithms (e.g. billing strategies)
* **Factory** – Object creation logic (e.g. create different Vehicle types)
* **Observer** – Notify components (e.g. sensor updates UI)

 ======================================================================================================




Here are some **classic and commonly asked Design Pattern interview questions**, especially in system design or object-oriented programming interviews:

---

## 🔁 **Common Design Pattern Interview Questions**

|  # | **Question**                                                                   | **Type**   | **Notes**                                                          |
| -: | ------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------------ |
|  1 | **What is a design pattern? Why are they useful?**                             | Conceptual | Start simple – show understanding of reusability & abstraction.    |
|  2 | **Explain the Singleton pattern. Where is it used?**                           | Creational | Very commonly asked – show thread-safe version.                    |
|  3 | **Factory vs Abstract Factory – What's the difference?**                       | Creational | Emphasize flexibility and decoupling object creation.              |
|  4 | **What is the Builder pattern? When would you use it?**                        | Creational | Good for complex objects (e.g., object with many optional params). |
|  5 | **Decorator vs Proxy pattern – Compare and contrast.**                         | Structural | Often asked to test deeper understanding.                          |
|  6 | **Explain Strategy vs State pattern.**                                         | Behavioral | Both use composition, often confused – highlight differences.      |
|  7 | **Implement an LRU Cache using design patterns.**                              | Applied    | Often solved with Singleton + Strategy + Observer mix.             |
|  8 | **Observer pattern – where have you used it?**                                 | Behavioral | UI frameworks, pub/sub systems.                                    |
|  9 | **When would you use the Command pattern?**                                    | Behavioral | Undo/Redo, queues, UI actions.                                     |
| 10 | **Which pattern would you use for a Vending Machine / ATM / Elevator system?** | Applied    | Great way to blend patterns with LLD questions.                    |

---

## 📌 **Bonus: Pattern → Real-World Mapping**

| **Pattern** | **Example Use Case**                          |
| ----------- | --------------------------------------------- |
| Singleton   | Database connection pool, logger              |
| Factory     | Notification service (SMS/Email/Push)         |
| Builder     | Creating complex objects like HTTP requests   |
| Observer    | UI frameworks, event-driven systems           |
| Strategy    | Payment processing, sorting algorithms        |
| Command     | Undo/redo functionality                       |
| Decorator   | Adding behavior to UI components              |
| Proxy       | Access control, lazy loading, network proxies |
| Adapter     | Integrating with legacy systems/APIs          |

---

Would you like **detailed explanations or code examples** for any of these (e.g., Factory pattern in Java)?
