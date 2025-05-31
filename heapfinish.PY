class MinHeap:
    def __init__(self, max_size):
        self.heap = [None] * max_size
        self.size = 0
        self.max_size = max_size

    def parent_index(self, i):
        return (i - 1) // 2

    def left_child_index(self, i):
        return 2 * i + 1

    def right_child_index(self, i):
        return 2 * i + 2

    def is_leaf(self, i):
        return self.left_child_index(i) >= self.size

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, task):
        if self.size >= self.max_size:
            print("Heap lleno")
            return

        self.heap[self.size] = task
        current = self.size

        while (current > 0 and
               self.heap[current]['priority'] < self.heap[self.parent_index(current)]['priority']):
            self.swap(current, self.parent_index(current))
            current = self.parent_index(current)

        self.size += 1

    def extract_min(self):
        if self.size == 0:
            return None

        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return popped

    def min_heapify(self, i):
        if not self.is_leaf(i):
            left = self.left_child_index(i)
            right = self.right_child_index(i)
            smallest = i

            if (left < self.size and
                self.heap[left]['priority'] < self.heap[smallest]['priority']):
                smallest = left

            if (right < self.size and
                self.heap[right]['priority'] < self.heap[smallest]['priority']):
                smallest = right

            if smallest != i:
                self.swap(i, smallest)
                self.min_heapify(smallest)

    def print_heap(self):
        for i in range(self.size):
            t = self.heap[i]
            print(f"{t['name']} ({t['priority']})", end=" | ")
        print()

    def print_heap_pretty(self):
        for i in range(self.size // 2):
            left = self.left_child_index(i)
            right = self.right_child_index(i)

            output = f"Parent: {self.heap[i]['name']} ({self.heap[i]['priority']})"
            if left < self.size:
                output += f" | Left: {self.heap[left]['name']} ({self.heap[left]['priority']})"
            if right < self.size:
                output += f" | Right: {self.heap[right]['name']} ({self.heap[right]['priority']})"
            print(output)

# Ejemplo de uso
if __name__ == "__main__":
    tareas = [
        { "name": "Enviar correo", "priority": 4 },
        { "name": "Preparar informe", "priority": 2 },
        { "name": "Reunión equipo", "priority": 5 },
        { "name": "Actualizar base de datos", "priority": 1 },
        { "name": "Revisar código", "priority": 3 },
    ]

    heap = MinHeap(20)

    print("📥 Insertando tareas:")
    for t in tareas:
        print(f"Insertando: {t['name']} con prioridad {t['priority']}")
        heap.insert(t)

    print("\n📋 Estado actual del heap:")
    heap.print_heap_pretty()

    print("\n📤 Extrayendo tareas en orden de prioridad:")
    while heap.size > 0:
        tarea = heap.extract_min()
        print(f"Tarea: {tarea['name']} | Prioridad: {tarea['priority']}")
