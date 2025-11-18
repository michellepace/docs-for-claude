![Logo Zustand](https://github.com/pmndrs/zustand/raw/main/docs/bear.jpg)

A small, fast, and scalable bearbones state management solution.
Zustand has a comfy API based on hooks.
It isn't boilerplatey or opinionated,
but has enough convention to be explicit and flux-like.

Don't disregard it because it's cute, it has claws!
Lots of time was spent to deal with common pitfalls,
like the dreaded [zombie child problem](https://react-redux.js.org/api/hooks#stale-props-and-zombie-children),
[React concurrency](https://github.com/bvaughn/rfcs/blob/useMutableSource/text/0000-use-mutable-source.md), and [context loss](https://github.com/facebook/react/issues/13332)
between mixed renderers.
It may be the one state manager in the React space that gets all of these right.

You can try a live demo [here](https://codesandbox.io/s/dazzling-moon-itop4).

[**Installation**](https://zustand.docs.pmnd.rs/getting-started/introduction#installation)

Zustand is available as a package on NPM for use:

```bash
# NPM
npm install zustand
# Or, use any package manager of your choice.
```

[**First create a store**](https://zustand.docs.pmnd.rs/getting-started/introduction#first-create-a-store)

Your store is a hook!
You can put anything in it: primitives, objects, functions.
The `set` function _merges_ state.

```js
import { create } from 'zustand'

const useBear = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 }),
  updateBears: (newBears) => set({ bears: newBears }),
}))
```

[**Then bind your components, and that's it!**](https://zustand.docs.pmnd.rs/getting-started/introduction#then-bind-your-components,-and-that's-it!)

You can use the hook anywhere, without the need of providers.
Select your state and the consuming component
will re-render when that state changes.

```jsx
function BearCounter() {
  const bears = useBear((state) => state.bears)
  return <h1>{bears} bears around here...</h1>
}

function Controls() {
  const increasePopulation = useBear((state) => state.increasePopulation)
  return <button onClick={increasePopulation}>one up</button>
}
```

[Edit this page](https://github.com/pmndrs/zustand/edit/main/docs/getting-started/introduction.md)