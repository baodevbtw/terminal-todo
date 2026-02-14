# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows [Semantic Versioning](https://semver.org/).

---

## [0.3.2] - 2026-02-14

### Changed
- Completed tasks are automatically sorted to the bottom

---

## [0.3.1] - 2026-02-14

### Fixed
- Automatically migrate old tasks.txt format (pre-0.3.0)
- Prevent crash when loading legacy task files

---

## [0.3.0] - 2026-02-14

### Added
- Mark tasks as done
- Show completion status in task list

### Changed
- Task file format now stores completion state
  (old tasks.txt is not compatible)

---

## [0.2.1] - 2026-02-14

### Added
- Confirmation prompt before deleting tasks

---

## [0.2.0] - 2026-02-14

### Added
- Persist tasks to disk using tasks.txt
- Load tasks automatically on startup

---

## [0.1.2] - 2026-02-14

### Added
- Delete tasks by number
- Handle invalid delete input safely

---

## [0.1.1] - 2026-02-14

### Fixed
- Prevent adding empty tasks

---

## [0.1.0] - 2026-02-14

### Added
- Initial terminal-based TODO application
- Add tasks via user input
- Display task list in terminal
- Basic command menu (add, quit)

### Notes
This is the first working version of the project.
All data is stored in memory and will be lost on exit.