
# Python CLI Alarm Clock

A command-line alarm clock application built in Python as part of a Senior Software Engineer build exercise.

## Overview

The goal of this exercise was not simply to build an alarm clock, but to demonstrate engineering decision-making, problem definition, architecture design, AI-assisted planning, implementation, and validation.

The requirements were intentionally open-ended, so the first step was to use AI to refine requirements, identify edge cases, evaluate trade-offs, and create an implementation plan before writing code.

## Features

- Add an alarm using HH:MM format
- List active alarms
- Cancel alarms by ID
- Persist alarms to JSON storage
- Alarm triggering with terminal notification
- Graceful shutdown using Ctrl+C
- Unit tests for business logic

## Project Structure

alarm_clock/
├── main.py            # Entrypoint
├── cli.py             # Typer CLI commands
├── alarm_manager.py   # Business logic (pure, no I/O)
├── scheduler.py       # Polling loop
├── alarm_models.py    # Alarm dataclass permanent string 
├── alarm_store.py     # JSON persistence
└── tests/
    └── test_alarm_manager.py 

## Architecture

### models.py

Contains the Alarm data model.

Responsibilities:
- Store alarm information
- Generate unique IDs
- Serialize and deserialize alarm data

### store.py

Handles persistence.

Responsibilities:
- Load alarms from JSON
- Save alarms to JSON
- Handle invalid or missing files gracefully

### alarm_manager.py

Contains business logic.

Responsibilities:
- Create alarms
- Validate alarm input
- List active alarms
- Cancel alarms
- Determine when alarms should fire

Design goal:
- Keep business logic separate from user interface and persistence concerns.
- Make logic easy to test.

### scheduler.py

Contains runtime scheduling loop.

Responsibilities:
- Poll alarms
- Trigger notifications
- Persist state changes
- Handle graceful shutdown

### cli.py

Provides the command-line interface.

Responsibilities:
- Parse user commands
- Display output
- Delegate work to business logic

### main.py

Application entrypoint.

Responsibilities:
- Start the CLI application

## Design Decisions

### JSON Persistence

Decision:
Use a JSON file instead of a database.

Reason:
The exercise explicitly excludes databases. JSON provides simple persistence while keeping the implementation lightweight and easy to inspect.

### UUID-Based Alarm IDs

Decision:
Generate short UUID-based identifiers.

Reason:
Allows alarms to be referenced and cancelled easily from the command line.

### Typer for CLI

Decision:
Use Typer for command handling.

Reason:
Provides:
- Automatic help documentation
- Type hints
- Simple command structure
- Minimal boilerplate

### Active Flag Instead of Deletion

Decision:
Cancel alarms by marking them inactive.

Reason:
Preserves alarm history and avoids modifying collection structure unnecessarily.

### Injectable Clock

Decision:
Allow check_and_fire() to receive the current time.

Reason:
Improves testability by avoiding dependence on the system clock.

### Polling Scheduler

Decision:
Poll every second.

Reason:
Simple, understandable, and sufficient for a CLI alarm clock.

## Requirements Refinement

Before implementation, AI was used to help refine requirements and identify a reasonable scope.

### Included

- Alarm creation
- Alarm listing
- Alarm cancellation
- Alarm triggering
- Persistence
- Unit tests

### Explicitly Excluded

- GUI
- Web interface
- Database
- Recurring alarms
- Snooze functionality
- Time zone management
- Mobile notifications

These exclusions were intentional to keep the solution focused and achievable within the exercise constraints.

## Design Review Findings

Before implementation, the proposed design was reviewed to identify weaknesses and trade-offs.

Key findings:

- Time representation using HH:MM is simple but limited.
- JSON persistence is suitable for this exercise but not ideal for concurrent access.
- File locking and atomic writes would be required for production-grade reliability.
- Injecting the current time improves testability significantly.
- Business logic should remain separate from CLI concerns.

The implementation incorporates the improvements that provided the highest value relative to complexity.

## Future Improvements

If this were extended into a production application, the next improvements would include:

- Full datetime support
- Recurring alarms
- Snooze functionality
- Atomic file writes
- File locking
- Dedicated application data directory
- Desktop/OS notifications
- REST API support
- Event-driven scheduling

## Running the Application

Install dependencies:

bash pip install typer pytest 

Add an alarm:

bash python main.py add 09:30 "Standup Meeting" 

List alarms:

bash python main.py list 

Cancel an alarm:

bash python main.py cancel <alarm_id> 

Start the scheduler:

bash python main.py run 

## Running Tests

bash pytest tests/ -v 

## AI Usage

AI was used throughout the planning and design phases to:

- Refine ambiguous requirements
- Identify edge cases
- Review architectural decisions
- Evaluate trade-offs
- Create an implementation plan
- Review the design before coding

All implementation decisions, scope decisions, validation, testing, and final code review were performed as part of the development process.

## Summary

This project focuses on demonstrating:

- Problem definition
- Engineering trade-offs
- Architecture design
- Separation of concerns
- Testability
- Incremental development
- AI-assisted engineering workflow

rather than maximizing feature count.



