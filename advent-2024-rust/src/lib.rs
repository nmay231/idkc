#![feature(assert_matches)]
#![feature(box_patterns)] // TODO: Replace with deref patterns when implemented for boxes
mod libs;

pub use libs::coin_change::CoinChange;
pub use libs::direction::Direc;
pub use libs::disjoint_set::{
    Count, DisjointSet, DisjointSetWithCount, Eve, EveAsIndex, EveOrNode,
};
pub use libs::point::Point;
pub use libs::zipper::{Zipper, ZipperTrait};

#[allow(deprecated)]
pub use libs::deprecated_points::{IsizePoint, UsizePoint};
