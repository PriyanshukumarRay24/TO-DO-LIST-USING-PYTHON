# 📝 To-Do List App (Tkinter)

A simple desktop To-Do List application built with Python's `tkinter` library. It lets you add, mark, and delete tasks through a clean GUI window.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- `tkinter` (comes pre-installed with standard Python distributions)

### Running the App

```bash
python todo.py
```

---

## 🖥️ Features

| Feature | Description |
|--------|-------------|
| ➕ Add Task | Type a task and click **ADD** to insert it into the list |
| ✅ Mark Task | Select a task and click **MARK** to append a ✓ checkmark |
| 🗑️ Delete Task | Select a task and click **DELETE** to remove it |

---

## 📖 How to Use

### Adding a Task
1. Click on the **entry field** (text box at the top).
2. Type your task (e.g., `Buy groceries`).
3. Click the **ADD** button.
4. The task will appear in the list below.

### Marking a Task as Done
1. **Click on a task** in the list to select/highlight it.
2. Click the **MARK** button.
3. The task will move to the bottom of the list with a ✓ appended (e.g., `Buy groceries ✓`).

### Deleting a Task
1. **Click on a task** in the list to select/highlight it.
2. Click the **DELETE** button.
3. The task will be permanently removed from the list.

---

## ⚠️ Common Usage Notes

- **You must select a task** before clicking MARK or DELETE, otherwise the app will throw an error (no item is selected).
- Tasks are **not saved** when you close the app — everything resets on relaunch.
- Marked tasks are moved to the **end of the list**, not kept in their original position.
- You can only select **one task at a time** for marking or deleting.

---

## 📁 Project Structure

```
todo-app/
│
└── todo.py       # Main application file
```

---

## 🛠️ Built With

- [Python](https://www.python.org/) — Programming language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — Standard Python GUI library

---

## 🔮 Possible Future Improvements

- Save tasks to a file (`.txt` or `.json`) so they persist after closing
- Edit existing tasks
- Add due dates or priority levels
- Keyboard shortcuts (e.g., `Enter` to add a task)
- Color-code completed vs pending tasks

---

## 📄 License

This project is open-source and free to use for personal or educational purposes.


![image alt](https://github.com/PriyanshukumarRay24/TO-DO-LIST-USING-PYTHON/blob/d28cff5470e6228ceead188cbc116a8dad51f6b0/todo%20list.png)
