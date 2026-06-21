from langchain.messages import HumanMessage

from src.Agent import AgentChef



def Non_Interractive_Demo():
    config = {"configurable": {"thread_id": "chef_demo"}}

    def chat(message: str):
        response = AgentChef.invoke(
            {"messages": [HumanMessage(content=message)], "preferences": []},
            config,
        )
        print(f"\nUser  : {message}")
        print(f"Chef  : {response['messages'][-1].content}")


        print("=" * 60)

    print("DEMO : Agent Chef Cuisinier Personnel")
    print("=" * 60)

    # Enregistrer les preferences
    chat("Je suis vegetarien et j'adore la cuisine espagnole.")
    chat("Je suis allergique aux poissons.")

    # Suggestions avec les ingredients disponibles
    chat(
        "J'ai dans mon frigo : des pates, des tomates, de l'ail, du filet de poisson "
        "de l'huile d'olive, du basilic et du parmesan. "
        "Qu'est-ce que je peux cuisiner ?"
    )

    # Suivi avec de nouveaux ingredients
    chat("Et si j'ajoute des oeufs et des epinards, qu'est-ce que je peux faire ?")
      

def Interractive_mode():
    config = {"configurable": {"thread_id": "chef_demo"}}

    while True:
        print("*"*60)
        print("**Entrer votre message. bye for quitting....")
        message = input("User:")
        if(message.lower() == "bye"):
            break
        else:
            response = AgentChef.invoke(
            {"messages": [HumanMessage(content=message)], "preferences": []},
            config,
        )
            print(f"Chef  : {response['messages'][-1].content}")

if __name__ == "__main__":
    print("*"*60)
    print("Demo : Personal Chef")
    print("*"*60)
    
    while True:
        print("1. Mode automatique (Execution automatique)")
        print("2. Mode interractive (Utilisateur peut interagir avec l'agent)")
        print("3. Quitte")
        print("Choisir le mode que vous voullez utiliser.")
        choice = input()

        match choice:
            case "1":
                print("-"*60)
                print("Mode automatique.............")
                print("-"*60)
                Non_Interractive_Demo()
                break
            case "2":
                print("-"*60)
                print("Mode interractive")
                print("-"*60)
                Interractive_mode()
            case "3":
                print("Bye")
                break
            case _:
                print("Valeur incorrect")
                
                
    