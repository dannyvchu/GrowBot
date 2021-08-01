# Growbot v0.9


# Create variables per plant and config (json)
# Regular check
    # Moistness
    # Temp
    # (water level)
    # Ambient light
# Log all measurements into csv
    # Create list of instructions from log
        # If moist < a for x time, initiate pump
        # Email moment any problems arise
# Run statistical analysis on data
    # over past 24hrs (max, min, avg)
        # moistness
        # temp/rh
        # ambient light
        # time lapse
    # same for weekly and monthly average
# Email at end of day results of log


## Goals
- **Keep plants alive**
    - Choose 1-2 plants and focus on collecting a good dataset
    - Fast growing plants...?
        - Quicker cycle for faster design iteration
        - Reactive
          - Sensitive to external influences
          - Very emotional plant 
        -  Easy to find
        - Herbs?
            - Basil (4-6wks)
            - Parsley (continual harvest)
        - Spring onions
    - Monstera
      - Sensitive plant
      - Not easy to kill :)
- **Measure how well we're keeping the plants alive**
    - Create timelapse video of plant growth
    - Feel the plant
    - If it needs sunlight, plants tend to grow lanky than it is growing leaves
- **Control methods to influence plant growth**
    - How much water
    - How frequently watered
    - Soil types
    - Additives, fertilizer
    - Control light exposure
        - LED grow lights
        - Grow in closet
- **Measure external influences**
    - sunlight meter
    - humidity meter
    - temperature meter
    - conductivity meter
    - co2 meter(?)



## Components

### Compute
- Raspberry Pi 
- Stepper Driver
  - https://www.sparkfun.com/products/12859
- GPIO Breakout Board
    - https://www.sparkfun.com/products/13717
- Relay Board
  - https://smile.amazon.com/Qunqi-Channel-Optocoupler-Expansion-Raspberry/dp/B078478SZ9/ref=sr_1_6?dchild=1&keywords=relay+board+raspberry+pi&qid=1626646070&sr=8-6

### Fluids 
- Peristaltic Pump
  - https://www.amazon.com/INTLLAB-Corrosion-Resistant-Peristaltic-Self-Priming/dp/B082K6CYV1/ref=sr_1_8?dchild=1&keywords=Peristaltic%2BPump&qid=1626645471&sr=8-8&th=1 
  - https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Peristaltic_pump.gif/220px-Peristaltic_pump.gif 
- Clear tubing
- Tubing fittings
- Fixturing + Motor Mount (3D Print)
- Valve
    - https://www.amazon.com/Beduan-Normally-Closed-Electric-Solenoid/dp/B07N2DZ5FP/ref=sr_1_6?dchild=1&keywords=tubing+valve+solenoid&qid=1626645695&sr=8-6 

### Instrumentation
- Atmospheric Sensing
    - Pressure, Altitude, Temp, Humidity
    - https://www.sparkfun.com/products/13676
- Soil Moisture Content
    - https://www.sparkfun.com/products/13637 
    - Tutorial: https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide?_ga=2.23594620.736241915.1626641403-768048569.1626641403#introduction 
- Ambient Light
  - https://www.sparkfun.com/products/8688

### Environment
- Lights
  - https://smile.amazon.com/BLOOMSPECT-Spectrum-Samsung-Dimmable-Greenhouse/dp/B08CZCDYR3/ref=sr_1_12?dchild=1&keywords=led+grow+light&qid=1626647047&sr=8-12


## Software Architecture

### Low Level
- Raspberry Pi GPIO
  - Stepper Motor Driver for Peristaltic Pump
  - I2C for sensors
  - GPIO Analog Inputs for other sensors

### Scheduler
- Sequences all events

### Visualizer
- @Danny to manage SQL database, connection
- Tableau
- Data sanitization
- Graphs, reporting

### Webpage
- Remote Control
- Displays KPI (Key Performance Indicators)