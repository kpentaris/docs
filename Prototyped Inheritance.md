Prototyped inheritance in Javascripts works as following:

 * Create a base class by creating a function constructor:
   function base() { this.a = 1; }
 * Create a subclass again by creating another function constructor:
   function sub() { this.b = 2; }
 * Now we need to declare that the `sub` class will be extending the base class. Javascript, essentially starts from the deepest
   object in the inheritance tree and if it doesn't find what it's looking for it checks under that object's `__proto__` property.
   In order to declare inhertance we must thus create that prototype chain.
 * To chain `sub` to `base` we do the following:
   - Create an *object* of the *prototype* property of the `base` function constructor using:
       Object.create(base.prototype)
     Remember that *prototype* property is a property of the *Function* object that is part of the Javascript api. That property
     is populated when the *Function* object's constructor is called with an object literal that has only one property named
     *constructor* and contains the function that is created from the *new Function* call.
     This essentially create an *empty* {} object literal (since we don't really call the `base` function) which *however* contains
     information on its own prototype chain under a __proto__ property. 
     We have thus  created an empty object which carries the previous links of the chain.
   - Assign that created object to `sub` function's *prototype* property. Now `sub` is chained to `base` which might be chained to
     something else. It is very important to understand why we use `Object.create(base.prototype)` and not `new base()`. If we used
     the constructor then we would also get an object literal instantiated with its properties, in our case {a: 1}. We *don't want that*.
     What we want is an empty object *simply which simply carries its own prototype chain*.
   - After linking `sub` with `base` we must not forget to reset `sub`'s constructor property to its own function.
     Using Object.create(base.prototype) -> {constructor: base, __proto__: <chain info>}. We only want the chain info. We thus reset
     the constructor property to `sub`:
       sub.prototype.constructor = sub
 * When we use the `new` keyword in Javascript followed by a constructor function what the VM does is create an empty object literal
   and assign it to the `this` keyword inside the called function's scope. Thus the `this` object receives any property that this
   constructor function assigns to it. In the case of var s = new sub(), s will *only* receive the `b` property! If we wanted to also
   receive the `a` property (which is usually the case) then we must explicitly also link the constructor calls (which other languages
   like Java do automatically) by declaring `sub` like so: function sub() {base.call(this); this.b = 2; }
 * After calling the constructor function, Javascript takes the produced `this` object (in our case {b: 2}) and on its *__proto__*
   field sets the constructor function's *prototype* property. This means that we now have an object literal with some primitive fields
   which has become part of the prototype chain of `sub` and `base`.
 * By adding a method to `sub.prototype` object, we can make it available to the created `sub` instance. This is because even though
   on the base literal s = {b:2} Javascript won't find the method, it will then go to the __proto__ field which points to `sub.prototype`
   and it will find it there. And even if it didn't find it there (because it was declared on `base.prototype`) then it will go to
   sub.__proto__ which points to `base.prototype` (due to Object.create(base.prototype)).
 * We are now done. Remember that in Javascript the chain of an instance of a class is the following:
   {propA, propB, propC} -> {methodOfSub} -> {methodOfBase} -> {methodOfObject}
   Essentially all Javascript class instances aren't of the type of the class. They are untyped object literals containing only
   primititve properties and their first link in the prototype chain is the class they come from.
