import melee
import argparse
import signal
import sys

# Project SUPRA - Basic libmelee Agent
# This script initializes Dolphin and connects a virtual controller.

def signal_handler(sig, frame):
    print("Shutting down Project SUPRA agent...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    parser = argparse.ArgumentParser(description='Project SUPRA Phase 1 Agent')
    parser.add_argument('--iso', help='Path to SSBM ISO', default='/app/iso/ssbm.iso')
    args = parser.parse_args()

    print("--- Project SUPRA: Phase 1 Agent Initializing ---")
    
    # Initialize Dolphin console
    # In a headless environment, we'd point this to the Slippi Dolphin path
    console = melee.Console(path="/usr/bin/dolphin-emu")
    
    # Port 1: The AI Agent
    controller = melee.Controller(console=console, port=1)
    
    # Start Dolphin
    console.run(iso_path=args.iso)
    print("Connecting to Dolphin...")
    console.connect()
    controller.connect()

    print("Agent connected. Entering main loop...")
    
    # Basic loop to keep the process alive and log stats
    frame_count = 0
    while True:
        gamestate = console.step()
        if gamestate is None:
            continue

        # Log frame data every 600 frames (~10 seconds)
        if frame_count % 600 == 0:
            print(f"Frame {frame_count}: Game State {gamestate.menu_state}")
            # Here we would feed data into our Personality Engine (BigQuery)
        
        # Placeholder for AI logic
        # if gamestate.menu_state == melee.Menu.IN_GAME:
        #    agent_logic(gamestate, controller)
        
        frame_count += 1

if __name__ == "__main__":
    main()
