# LAB 7 - Creating an agent HITL (Human in the loop)
## Objectif
Implementing an AI agent whose execution can be interrupted to request human validation before continuing — using LangGraph.
## Concept

Agent HITL (Human-in-the-Loop) is a collaborative approach where human oversight is purposefully built into an AI agent's workflow. Instead of acting completely autonomously, the agent pauses execution at critical decision points to wait for a human to approve, reject, or edit its proposed actions.

## The decisions

|Type 	|Behavior 	|Extra param|
|------|--------------|--------------------------|
|"approve" 	|Sending email as it is 	|—
|"reject" 	|Cancel and sends the reason| 	"message": "..."|
|"edit" 	|Replace all arguments and send the updated email |	"edited_action": {"name": ..., "args": {...}}|

## Note
* Project require an active ollama server
