module test

import math

[export: 'square']
fn square(i int) int {
	return i * i
}

[export: 'sqrt_of_sum_of_squares']
fn sqrt_of_sum_of_squares(x f64, y f64) f64 {
	return math.sqrt(x * x + y * y)
}

[export: 'hello']
fn hello(name &u8) &u8 {
	v_name := unsafe { name.vstring() }
	println("side v: $v_name")
	text := 'hello, $v_name!'.u8()
	return &text
}
