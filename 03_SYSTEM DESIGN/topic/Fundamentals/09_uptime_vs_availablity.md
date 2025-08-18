Great question — **uptime** and **availability** are related but **not the same**. They both measure aspects of system reliability, but from slightly different angles.

---

## ✅ Uptime

**Uptime** refers to the **total amount of time** a system, server, or service has been **running without interruption**.

* It is typically expressed as a **raw duration or percentage** over a time period.
* Think of it as **“How long has the system been up?”**

### Example:

> A server has been running without a restart for **360 hours** this month.
> If the month has 720 hours total, uptime is:
> `360 / 720 = 50%`

---

## ✅ Availability

**Availability** refers to the **percentage of time** a system is **fully operational and accessible** when needed.

* Includes not just whether it's "up" but whether it's also **usable**.
* It considers **planned and unplanned downtime** (e.g., maintenance, network issues).
* Usually expressed as a **percentage**, e.g., 99.9% ("three nines").

### Formula:

```text
Availability (%) = (Total Time - Downtime) / Total Time × 100
```

---

## 🔄 Key Differences

|                | **Uptime**                 | **Availability**                            |
| -------------- | -------------------------- | ------------------------------------------- |
| Measures       | Time system is up          | Time system is available/usable             |
| Includes       | Just operational time      | Also considers scheduled downtime, failures |
| Expressed as   | Duration or %              | % only                                      |
| Example metric | "Server uptime: 720 hours" | "Availability: 99.95%"                      |

---

## 🧠 In Real-World Terms

* A system could have **100% uptime** (no crashes), but if it's under **maintenance and users can't access it**, the **availability drops**.
* Conversely, a system could have **99.9% availability**, even if it's restarted once a month, as long as downtime is brief.

---

Let me know if you’d like a visual chart or how this is tracked in cloud platforms like AWS or Azure.
