#ifndef _POINT_HPP
#define _POINT_HPP


class Point {
	int x,
		y,
		z;

	public:
		Point() = delete;
		Point(int a, int b, int c)
			: x(a), y(b), z(c)
		{ }

	void print();

	friend double getDistance(const Point& a, const Point& b);
};


double getDistance(const Point& a, const Point& b);



#endif /* _POINT_HPP */