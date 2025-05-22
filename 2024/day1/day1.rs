use std::fs;
use std::collections::HashMap;

fn main()  {
    let contents = fs::read_to_string("input.txt")
        .expect("Should be able to read input");

    let input_vec: Vec<&str> = contents.split("\n").collect();

    println!("p1: {}", solution(&input_vec));
    println!("p2: {}", solution2(&input_vec));
}

fn solution(inp_vec: &Vec<&str>) -> i32 {
    let n = inp_vec.len() - 1;
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for input in inp_vec {
        let left_right: Vec<&str> = input.split_whitespace().collect();
        if left_right.len() != 0 {
            left.push(left_right[0].parse::<i32>().unwrap());
            right.push(left_right[1].parse::<i32>().unwrap());
        }
    }
    left.sort();
    right.sort();
    let mut result: i32 = 0;
    for n in 0..n {
        result += i32::abs(left[n] - right[n]);
    }
    return result;
}


fn solution2(inp_vec: &Vec<&str>) -> i32 {
    let n = inp_vec.len() - 1;
    let mut left: Vec<i32> = Vec::new();
    let mut right_count = HashMap::new();
    for input in inp_vec {
        let left_right: Vec<&str> = input.split_whitespace().collect();
        if left_right.len() != 0 {
            left.push(left_right[0].parse::<i32>().unwrap());
            let right_val : i32 = left_right[1].parse::<i32>().unwrap();
            let count = right_count.entry(right_val).or_insert(0);
            *count += 1;
        }
    }
    let mut result: i32 = 0;
    for n in 0..n {
        let val = left[n];
        let count = right_count.get(&val).copied().unwrap_or(0);
        result += i32::abs(left[n] * count);
    }
    return result;
}