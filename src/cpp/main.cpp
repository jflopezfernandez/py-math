
#include "includes/Main.hpp"


int main()
{
	Point o(0,0,0);
	o.print();

	Point p(7,24,0);
	p.print();

	double dist = getDistance(o,p);
	std::cout << "Distance: " << dist << std::endl;

	return 0;
}