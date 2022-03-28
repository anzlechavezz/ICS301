// problem at hand: from an input, calculate the 2 roots of a quadratic equation.
//
// Variables required:
// int d;
// int roots[x1, x2];
// int [a, b, c]
//
// Steps;
// int a <- input "what is the a?"
// int b <- input "what is the b?"
// int c <- input "what is the c?"
//
// int d <- ( b ^ 2 - 4 * a * c ).sqrt()
//
// vec roots.push {
//     x1 <= (-b+d)/2a
//     x2 <= (-b-d)/2a
// }

extern crate nalgebra as na;

fn main() {
    let (a, b, c): (f64, f64, f64) = (1.0, 5.0, 6.0);

    // note: powf() is for floating point integers, required for square root.
    let mut d: f64 = (b.powf(2.0)) - 4.0 * a * c ;
    println!("{:?}", d.sqrt()); 


    let x1: f64 = (-b-d) / 2.0 * a;

    let x2: f64 = (-b+d) / 2.0 * a;

    println!("{}, {}", x1, x2)
}
