# GPT-Simulation
ChatGPT 3.5 Turbo based character interaction simulation. This program provides a configurable simulation between GPT powered avatars through text. 

Still under development!

### GPTInstance
A GPTInstance refers to an instance of the ChatGPT session. Each GPTInstance is trained individually based on its pre-configured attributes and the attributes of other GPTInstances it knows of in the simulation. This ensures that each avatar is unique and responds differently to various stimuli.

There are two types of GPTInstances:
 1. **Narrator**:  This instance operates on an event/time-based system, where it records and tracks key events from each day and moves time forward accordingly. There is only one Narrator instance per GPT Pool, and it serves as a crucial component for keeping track of time and events in the simulation.
 2. **Character**: A Character avatar is designed to interact with the surrounding world and other instances. It is programmed be highly opinionated and dynamic, free from any restraints imposed by pre-possessed knowledge. This instance type adds a layer of realism to the simulation by allowing avatars to react to various stimuli based on their individual personalities and biases.

All character based GPTInstances are configured to share the following traits:
 - Upon initialization, GPTInstance automatically toggles certain attributes about itself as static or dynamic.
 - GPTInstance may have hidden attribute that are revealed through interactions with other GPTInstances.
 - GPTInstance retains past memories based on the "assistant" and "user" configuration and will plan for the future based on past events.

### GPT Pool
The GPT Pool is a simulation of the world which GPTInstances resides in. The GPT Pool dynamically generates certain (large) events and relay it to the narrator GPTInstance. A GPT Pool generally contains multiple character GPTInstances. 
