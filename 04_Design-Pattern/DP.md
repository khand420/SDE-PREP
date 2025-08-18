Here’s a curated list of **important design pattern interview questions**, especially relevant for **backend, system design, and object-oriented interviews**. These are frequently asked in companies like Amazon, Microsoft, Flipkart, and startups.

---

## 🔥 **Top Design Pattern Interview Questions**

---

### 🔁 1. **What are design patterns? Why are they useful?**

* Define design patterns as proven solutions to common software design problems.
* Mention categories: Creational, Structural, Behavioral.
* Benefits: reusable, proven, increases maintainability, improves communication.

---

### 🏗️ 2. **What are the main types of design patterns?**

* **Creational** – How objects are created
* **Structural** – How classes/objects are composed
* **Behavioral** – How objects interact

---

### 🧰 3. **Explain the Singleton pattern. When would you use it?**

* Only one instance of a class exists (e.g., Logger, Config).
* Thread-safe implementation is important.
* Example: Database connection pool, application-wide cache.

---

### 🏭 4. **What is the Factory pattern? How is it different from Abstract Factory?**

* **Factory Method** – Creates objects based on input/condition.
* **Abstract Factory** – Creates *families* of related objects.
* Used when object creation logic should be separated from the main logic.

---

### 🧩 5. **Explain the Strategy pattern with a real-world example.**

* Defines a family of interchangeable algorithms.
* Example: Different payment methods (UPI, card, wallet).
* Context class uses one of the strategies dynamically.

---

### 🛠️ 6. **What is the Observer pattern?**

* One-to-many dependency between objects.
* When one changes, all dependents are notified.
* Real-world: Event listeners, UI update subscriptions.

---

### 🏗️ 7. **What is the Decorator pattern?**

* Add new behavior to an object **without altering its structure**.
* Example: Add tax or discount calculations to a base order object.
* Often used for wrapping.

---

### 🔁 8. **What is the difference between the Adapter and Facade patterns?**

* **Adapter**: Makes one interface compatible with another (e.g., legacy system wrapper).
* **Facade**: Simplifies a complex subsystem with a unified interface.

---

### 🪜 9. **Explain the Command pattern. Where is it used?**

* Encapsulate a request as an object.
* Supports undo, logging, and queuing.
* Example: Button clicks in GUI, job queues.

---

### 🪝 10. **What is the Template Method pattern?**

* Base class defines a skeleton of an algorithm.
* Subclasses fill in specific steps.
* Used to enforce a sequence of steps with custom behaviors.

---

### 👣 11. **What is the Builder pattern?**

* Used to build complex objects step by step.
* Example: Constructing an object like a `Meal` with drinks, main, dessert.
* Helps avoid telescoping constructors.

---

### 🔒 12. **What is the Proxy pattern?**

* A placeholder or surrogate for another object.
* Example: Virtual proxy for lazy loading, security proxy, logging proxy.

---

### 🔁 13. **What is the difference between Composition and Inheritance?**

* Composition is **"has-a"**, Inheritance is **"is-a"**.
* Prefer composition for flexibility and lower coupling.

---

### 💡 14. **Can you name some patterns used in frameworks (Spring, Django, etc.)?**

* **Spring**: Singleton (beans), Proxy (AOP), Template (JdbcTemplate), Factory
* **Django**: MVC (Model-View-Controller)

---

## ✅ Bonus Questions

| Question                                                      | Why It's Asked                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------- |
| When would you **not** use a Singleton?                       | Shows awareness of pitfalls (e.g., testability, hidden state) |
| What’s the difference between **Composition vs Inheritance**? | Fundamental OOP question                                      |
| Have you ever implemented a custom design pattern?            | Checks real-world application                                 |
| Explain real use cases where you used patterns in production  | To validate experience, not memorization                      |

---

Would you like flashcards, real-world examples, or code snippets for these patterns?
