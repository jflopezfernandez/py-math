
#include "includes/Main.hpp"


void Point::print()
{
	printf("(%i,%i,%i)\n", x, y, z);
}


double getDistance(const Point& a, const Point& b)
{
	double x = (double) (b.x - a.x) * (b.x - a.x);
	double y = (double) (b.y - a.y) * (b.y - a.y);
	double z = (double) (b.z - a.z) * (b.z - a.z);

	return (sqrt(x + y + z));
}