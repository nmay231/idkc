type Output = usize;

fn part1(text: &str) -> Output {
    0
}

fn part2(_text: &str) -> Output {
    0
}

fn main() -> std::io::Result<()> {
    let text = std::fs::read_to_string("./assets/day%DAY_NUMBER%.txt")?;

    println!("part 1 result = {:?}", part1(&text));
    println!("part 2 result = {:?}", part2(&text));

    Ok(())
}

// #[cfg(test)]
// mod tests {
//     use crate::part1;
//     use indoc::indoc;
//
//     const TEXT1: &str = indoc! {"
//         asdf
//     "};
//
//     #[test]
//     fn part1_given_example() {
//         assert_eq!(part1(TEXT1), 0);
//     }
//
//     #[rstest::rstest]
//     #[case(TEXT1, 0)]
//     fn part1_given_examples(#[case] text: &str, #[case] expected: usize) {
//         assert_eq!(part1(text), expected);
//     }
// }
