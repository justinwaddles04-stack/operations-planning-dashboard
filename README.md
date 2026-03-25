# Change Management & Operations Planning Analysis
### GRC Portfolio Project

---

## Scenario

Midwest Regional Health Network operates under HIPAA and SOC 2 compliance 
requirements that mandate a formal change management process for any 
modifications to systems handling PHI. Uncontrolled changes to clinical 
and operational systems are a leading cause of security incidents and 
audit findings.

I built this project to simulate how an analyst would monitor operational 
demand patterns, assess inventory risk, and track the status of operational 
changes through a structured change control process — the kind of work 
that sits at the intersection of operations and GRC.

---

## What I Did

Using Python (Pandas, NumPy, Matplotlib) I analyzed 6 months of demand 
data across three product lines (SKU-A, SKU-B, SKU-C), calculated reorder 
points and safety stock levels using lead time data, flagged inventory 
reorder risks, and tracked operational changes through a structured 
change control log.

This mirrors two real GRC workflows: operational risk monitoring (are we 
about to run out of something critical?) and change management tracking 
(are changes moving through the approval process in a controlled way?).

---

## Key Findings

**SKU-A demand grew consistently from 120 to 160 units over 6 months — 
a 33% increase — while current inventory stayed flat at 300 units.** 
With a 7-day lead time, the reorder point calculation flags this product 
as approaching reorder territory. If demand continues trending upward, 
the static inventory level will become a supply chain risk within 
the next quarter.

**SKU-C has the longest lead time at 14 days**, meaning it requires the 
most forward planning of the three products. Despite relatively low 
demand (60–82 units), the extended lead time increases its reorder 
point and makes it the most operationally fragile SKU in a disruption 
scenario.

**The change control log shows all four change statuses represented: 
Pending Approval, Approved, In Review, and Implemented — one each.** 
In a real environment this distribution would indicate a change pipeline 
that is moving, but slowly. No changes are stuck or stalled, but the 
even distribution suggests a small, early-stage change management 
process rather than a mature one with volume and velocity.

---

## Connection to GRC

Change management is a formal control requirement under multiple 
frameworks that GRC analysts work with daily:

- **SOC 2 (CC8.1)** — requires a formal change management process 
including authorization, testing, and approval before implementation
- **HIPAA Security Rule** — operational safeguards require that changes 
to systems handling PHI are controlled and documented
- **NIST CSF (PR.IP-3)** — configuration change control processes are 
a core Protect function requirement

The change control log in this project directly simulates the kind of 
documentation a GRC analyst would review during an audit or 
compliance assessment.

---

## Files

| File | Description |
|------|-------------|
| `demand_inventory_analysis.py` | Python script for demand analysis, reorder point calculations, and inventory risk flagging |
| `monthly_demand.csv` | Raw demand dataset across 3 SKUs over 6 months |
| `change_status_summary.csv` | Change control log tracking status of operational changes |
| `demand_trends.png` | Visualization of monthly demand trends by product |
| `requirements.txt` | Python dependencies |

---

## Frameworks Referenced

- **SOC 2 Trust Services Criteria** — CC8.1 Change Management
- **HIPAA Security Rule** — Operational Safeguards
- **NIST CSF** — Protect function, PR.IP-3 Configuration Change Control

---

*This is a fictional scenario created for portfolio purposes.
No real patient data or organizational information was used.*
