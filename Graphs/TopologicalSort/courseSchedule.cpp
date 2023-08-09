// ### COURSE SCHEDULE

// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given 
// an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you
//  want to take course ai.

// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.

// https://leetcode.com/problems/course-schedule/description/

// time complexity - O(V + E)
// space complexity - O(V + E)
class Solution {
public:
    vector<vector<int>> buildAdjacencyList(int noOfNodes, vector<vector<int>>& edgeList) {

        vector<vector<int>> adjList (noOfNodes);
        for (int i = 0; i < edgeList.size(); i++) {
            vector<int> edge = edgeList[i];
            adjList[edge[1]].push_back(edge[0]);
        }

        // for (int i = 0; i < noOfNodes; i++) {
        //     cout << i << ": ";
        //     for (auto node: adjList[i]) {
        //         cout << node << " ";
        //     }
        //     cout << endl;
        // }

        return adjList;
    }

    bool dfs(vector<vector<int>>& adjList, vector<int>& state, int node) {
        //function returns if graph has a cycle

        // each vertex can have 3 different states:
        // state 0 -> vertex not visited yet (white)
        // state -1 -> vertex being processed i.e not all descendents processed yet or is till in function call state (gray)
        // state 1 -> vertex and all its descendents are processed (black)
        if (state[node] == 1) return false;
        if (state[node] == -1) return true;

        state[node] = -1;
        for (auto neighbour: adjList[node]) {
            if (dfs(adjList, state, neighbour) == true)
                return true;
        }

        state[node] = 1;
        return false;


    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        //vector<vector<int>> courses = buildAdjacencyList(numCourses, prerequisites);
        vector<vector<int>> courses (numCourses);
        for (int i = 0; i < prerequisites.size(); i++) {
            vector<int> edge = prerequisites[i];
            courses [edge[1]].push_back(edge[0]);
        }

        vector<int> state (numCourses, 0);

        for (int course = 0; course < numCourses; course++) {
            if (state[course] == 0) {
                if (dfs(courses, state, course) == true) return false;
            }
        }

        return true;      
    }    

    // Using Kahn's algorithm
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        //use kahn's algorithm
        vector<vector<int>> adjList = buildAdjacencyList(numCourses, prerequisites);

        //build indegree array
        vector<int> indegree (numCourses, 0);
        for (int i = 0; i < prerequisites.size(); i++) {
            vector<int> edge = prerequisites[i];
            indegree[edge[0]]++;
        }

        queue<int> q;
        for (int node = 0; node < numCourses; node++) {
            if (indegree[node] == 0)
                q.push(node);
        }

        // for (int i = 0; i < indegree.size(); i++) {
        //     cout << indegree[i] << " ";
        // }

        //vector<int> topoOrdering;
        int count = 0;
        while (q.size() > 0) {
            int course = q.front(); q.pop();
           // topOrdering.push_back(course);
            count++;

            for (auto neighbour: adjList[course]) {
                indegree[neighbour]--;
                if (indegree[neighbour] == 0) q.push(neighbour);
            }
        }

        if (count != numCourses) {
            return false;
        }
        return true;


};


