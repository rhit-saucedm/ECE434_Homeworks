# HW 6 Files
## Marco Saucedo

#### Julia Cartwright Video:
1. Works at National Instruments as a stable real-time developer.
2. It is a patch for the Linux kernel that provides support for real-time editing capabilities that is often used in embedded projects where a real-time OS is necessary.
3. Embedded projects can run two different types of tasks: Real-time sensitive tasks and non-latency specific tasks. Mixed Criticality systems, these tasks are run together.
4. If drivers are part of handling an interrupt, they cannot be threaded normally.
5. Delta is the latency between the time an event occurs and the time the application begins to respond to the event
6. It takes a timestamp, sleeps for a certain duration, and takes another timestamp.
7. Figure 2 shows a long histogram of cyclictest data. The purple line does not show a real time OS, and so there were spikes around 360us.
8. Dispatch: Time from the interrupt being called to the relevant hardware being woken up. Scheduling: Time for the CPU to execute the high-priority task that is scheduled
9. Mainline shows long running interrupts
10. The lower priority interrupt is being handled. The higher priority IRQ can only begin when the lower priority event has finished
11. The lower priority IRQ is interrupted and external events can begin to execute. The lower priority IRQ can begin after this is finished.

#### PREEMPT_RT 
Load from PREEMPT_RT Module:
bone$ **cd ~/exercises/linux/modules**
bone$ **make**
bone$ **make clean**

# hw06 grading

| Points      | Description | |
| ----------- | ----------- |-|
|  2/2 | Project | *IoT Weather Station*
|  4/5 | Questions | *Mainline is the main kernel tree.*
|  4/4 | PREEMPT_RT
|  0/2 | Plots to 500 us | *Only to 400*
|  5/5 | Plots - Heavy/Light load
|  2/2 | Extras
| 17/20 | **Total**

*My comments are in italics. --may*