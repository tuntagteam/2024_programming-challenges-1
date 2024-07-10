import heapq

def dijkstra(edges, start, end):
    graph = {}
    for edge in edges:
        u, v, w = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    queue = [(0, start)]
    distances = {start: 0}
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return current_distance

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return float("inf")

# รับข้อมูลจากผู้ใช้
edges_input = input("กราฟที่เป็นลิสต์ของคู่จุดเชื่อมต่อและน้ำหนักของการเชื่อมต่อแต่ละคู่: ")
edges = [tuple(map(int, edge.split())) for edge in edges_input.split(',')]
start = int(input("จุดเริ่มต้น: "))
end = int(input("จุดสิ้นสุด: "))

# หาทางเดินที่สั้นที่สุด
shortest_path_length = dijkstra(edges, start, end)
print("ความยาวของทางเดินที่สั้นที่สุด:", shortest_path_length)