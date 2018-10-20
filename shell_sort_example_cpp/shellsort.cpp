#include <iostream>
#include <vector>

using namespace std;

template<typename T>
ostream& operator<<(ostream & os, const vector<T> & v) {
	for (const auto &i : v) {
		os << i;
		os << "\t";
	}
	return os;
}

template <typename T>
void shell_sort(vector<T> &vi) {
	for (auto shell = vi.size()/2; shell > 0; shell /= 2) {
		for (auto i = 0; i < vi.size(); ++i) {
			for (auto j = i; j-shell > 0 && vi[j-shell] > vi[j]; j -= shell) {
				auto tmp = vi[j];
				vi[j] = vi[j-shell];
				vi[j-shell] = tmp;
			}
		}
	}
}

int main() {
	vector<int> vi{1, 3, 2, 10, 9, 7, 5, 8, 6, 4};
	shell_sort(vi);
	cout << vi << endl;
	return 0;
}
