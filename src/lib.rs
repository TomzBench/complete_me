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
        let mut mock = MockMyTrait::new();
        mock.expect_foo().with(predicate::eq(4)).times(1).returning(|x| x+1);
        assert_eq!(5, mock.foo(4));
    }
}
