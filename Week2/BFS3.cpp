#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

unordered_map<string, vector<string>> graph = {
    {"0", {"3", "4"}},
    {"1", {"6", "0"}},
    {"2", {"5", "6"}},
    {"3", {"7", "1"}},
    {"4", {"6"}},
    {"5", {"7", "6"}},
    {"6", {"4", "2"}},
    {"7", {"5"}},
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
    bfs("0");
    return 0;
}
