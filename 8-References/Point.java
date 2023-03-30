public class Point {
    private int x;
    private int y;

    // constructor, getters and setters, toString

    public double getDistance(Point p) {...} // computes the distance between two points

    public boolean equals(Point rhs) {
        return this.x == rhs.x && this.y == rhs.y;
    }
}

int x = 1;
int y = 2;

Point p = new Point(x, x + 1);
Point q = new Point(p.getX(), y);
Point r = p;

r.setY(4);


int x = 42;
int y;
y = x; // draw memory

Point p = new Point(1, 2);
Point q;
q = p; // draw memory
       // called an "alias"

q.setX(3);

System.out.println(p)
