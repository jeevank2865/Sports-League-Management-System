# 🏆 Sports League Management System (SLMS)

A full-stack **Django-based Sports League Management System** designed to manage tournaments, teams, players, matches, points tables, and role-based dashboards (Admin, Captain, Referee, Guest).

This project is suitable for **academic projects, mini/major projects, and real-world league management use cases**.

---

## 📌 Features

### 🔐 Role-Based Access Control
- **Admin**
  - Manage sports, tournaments, teams, players, matches
  - Assign captains to teams
  - Update match results
  - View points table
- **Captain**
  - View own team details
  - Add and manage players of own team
  - View points table
- **Referee**
  - Update match results
  - View teams, players, and points table
- **Guest**
  - View tournaments, teams, players, and points table

---

### 🏟️ Tournament Management
- Create multiple sports (Cricket, Football, etc.)
- Create tournaments under each sport
- Assign teams to tournaments

---

### 👥 Team & Player Management
- Create teams with assigned captains
- Add players to teams
- Restrict captains to manage only their own team

---

### 📝 Match Management
- Schedule matches between teams
- Update scores, winners, and Player of the Match (POM)
- Match status tracking (Scheduled / Completed)

---

### 📊 Points Table
- Automatic points calculation
- Tournament-wise ranking
- Wins, losses, draws, and total points

---

### 🎨 UI
- Clean and modern UI
- Separate dashboards for Admin, Captain, Referee, and Guest
- Responsive layout

---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|-----------|
| Backend     | Python, Django |
| Database    | MySQL |
| Frontend   | HTML, CSS, Bootstrap |
| Auth       | Django Authentication |
| ORM        | Django ORM |
| Version Control | Git & GitHub |

---

## 📂 Project Structure
