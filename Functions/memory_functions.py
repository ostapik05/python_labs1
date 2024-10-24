from ConstantsAndVariables.memory import memory

def memory_save(result):
    global memory
    memory = result
    print(f"Result {result} saved to memory.")

def memory_recall():
    global memory
    if memory is not None:
        print(f"Memory recall: {memory}")
        return memory
    else:
        print("Memory is empty.")
        return None

def memory_clear():
    global memory
    memory = 0  # Очищення пам'яті до 0
    print("Memory cleared.")

def memory_add(value):
    global memory
    if memory is None:
        memory = 0  # Якщо пам'ять не ініціалізована, встановлюємо її в 0
    memory += float(value)  # Переконайтеся, що додаємо значення як float
    print(f"Result {memory} added to memory.")