objective - to build python cli alarm clock 

Architecture :
alarm_clock/
├── main.py            # Entrypoint
├── cli.py             # Typer CLI commands
├── alarm_manager.py   # Business logic (pure, no I/O)
├── scheduler.py       # Polling loop
├── alarm_models.py    # Alarm dataclass permanent string 
├── alarm_store.py     # JSON persistence
└── tests/
    └── test_alarm_manager.py   

-- with no Database 



