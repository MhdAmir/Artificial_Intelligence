#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

unordered_map<string, vector<string>> graph = {
    {"1", {"3", "2"}},
    {"2", {"4", "5"}},
    {"3", {"6", "4"}},
    {"4", {"6", "8", "7", "5"}},
    {"5", {"7"}},
    {"6", {"9", "8"}},
    {"7", {"9"}},
    {"8", {"9"}},
    {"9", {}}
};

vector<string> visited;
queue<string> q; 

void bfs(string node) {
    visited.push_back(node);
    q.push(node);
    vector<string> m;

    while (!q.empty()) {
        std::cout << "OPEN" << std::endl;
        std::queue<std::string> q_copy = q;
        while (!q_copy.empty()) {
            std::cout << q_copy.front() << " "; 
            q_copy.pop();
        }
        std::cout << std::endl;
        std::cout << "=============" << std::endl;

        string m_simpan = q.front();
        m.push_back(q.front());
        q.pop();

        for (string neighbour : graph[m_simpan]) {
            if (find(visited.begin(), visited.end(), neighbour) == visited.end()) {
                visited.push_back(neighbour);
                q.push(neighbour);
            }
        }
        std::cout << "CLOSE" << std::endl;
        for(int i = 0; i < m.size();i++){
            cout << m[i] << " ";
        }
        cout << endl;

    }
}

int main() {
    cout << "Following is the Breadth-First Search" << endl;
    bfs("1");
    return 0;
}
