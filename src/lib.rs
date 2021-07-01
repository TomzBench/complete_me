use mockall::*;
use mockall::predicate::*;

#[automock]
trait MyTrait{
    fn foo(&self, x:u32)->u32;
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
        let mock = MockMyTrait::new();
    }
}
