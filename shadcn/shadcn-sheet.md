
# Shadcn Sheet

React sheet for slide-out panels and contextual sidebars with edge positioning and focus management. Built with TypeScript and Tailwind CSS for Next.js using Radix UI.

Table of Contents

Ever notice how the best mobile apps have those panels that slide in from the edges? That's what sheets do—they're like sidebars but way more flexible. Need a settings panel that slides in from the right? A notification bar from the top? A mobile-style bottom sheet? This shadcn/ui sheet handles all of that with the smooth animations users expect from your React applications.

### [Sheet showcase](https://www.shadcn.io/ui/sheet\#sheet-showcase)

Clean form in a contextual side panel:

Preview

Code

Source

Edit Profile

```
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function SheetDemo() {
  return (
    <div
      className="flex justify-center self-start pt-6 w-full"
      style={{
        all: 'revert',
        display: 'flex',
        justifyContent: 'center',
        alignSelf: 'flex-start',
        paddingTop: '1.5rem',
        width: '100%',
        fontSize: '14px',
        lineHeight: '1.5',
        letterSpacing: 'normal'
      }}
    >
      <Sheet>
        <SheetTrigger asChild>
          <Button variant="outline">Edit Profile</Button>
        </SheetTrigger>
        <SheetContent>
          <SheetHeader>
            <SheetTitle>Edit profile</SheetTitle>
            <SheetDescription>
              Make changes to your profile here. Click save when you're done.
            </SheetDescription>
          </SheetHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                Name
              </Label>
              <Input
                id="name"
                defaultValue="Pedro Duarte"
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="username" className="text-right">
                Username
              </Label>
              <Input
                id="username"
                defaultValue="@peduarte"
                className="col-span-3"
              />
            </div>
          </div>
          <SheetFooter>
            <SheetClose asChild>
              <Button type="submit">Save changes</Button>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>
  )
}
```

Sign in to view the code

[Sign in](https://www.shadcn.io/sign-in)

### Reactbutton

```
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...(props as any)}
    />
  )
}

export { Button, buttonVariants }
```

### Reactinput

### Reactlabel

### Reactsheet

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

Built on Radix UI Dialog with focus management and proper ARIA semantics. This free open source component handles the overlay, positioning, and animations while you focus on what goes inside. Styled with Tailwind CSS to match your design system instead of fighting z-index battles and animation timing.

```
npx shadcn@latest add sheet
```

## [Why sheets actually beat regular modals](https://www.shadcn.io/ui/sheet\#why-sheets-actually-beat-regular-modals)

Here's the thing—sheets feel way more natural than popup modals, especially on mobile. Think about how Instagram shows photo details, or how Spotify's now playing panel slides up from the bottom. Sheets keep the main content visible while adding contextual information, creating that native app feeling users expect.

Unlike modals that interrupt your workflow and demand full attention, sheets complement what you're already doing. Users can still see and interact with the main content while accessing secondary features. Plus they slide in from screen edges like real mobile apps, not pop up from the center like desktop software from 2005.

This free shadcn sheet handles the complex parts—focus trapping, keyboard navigation, edge positioning, smooth animations—while you focus on creating interfaces that feel modern and contextual. Whether you're building settings panels, navigation drawers, or mobile action sheets in your Next.js applications, sheets that slide naturally enhance user experience in your JavaScript projects.

## [Common sheet patterns you'll actually use](https://www.shadcn.io/ui/sheet\#common-sheet-patterns-youll-actually-use)

### [Settings and preferences panel](https://www.shadcn.io/ui/sheet\#settings-and-preferences-panel)

User configuration that slides in from the right:

Preview

Code

Source

Edit Profile

```
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function SheetDemo() {
  return (
    <div
      className="flex justify-center self-start pt-6 w-full"
      style={{
        all: 'revert',
        display: 'flex',
        justifyContent: 'center',
        alignSelf: 'flex-start',
        paddingTop: '1.5rem',
        width: '100%',
        fontSize: '14px',
        lineHeight: '1.5',
        letterSpacing: 'normal'
      }}
    >
      <Sheet>
        <SheetTrigger asChild>
          <Button variant="outline">Edit Profile</Button>
        </SheetTrigger>
        <SheetContent>
          <SheetHeader>
            <SheetTitle>Edit profile</SheetTitle>
            <SheetDescription>
              Make changes to your profile here. Click save when you're done.
            </SheetDescription>
          </SheetHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                Name
              </Label>
              <Input
                id="name"
                defaultValue="Pedro Duarte"
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="username" className="text-right">
                Username
              </Label>
              <Input
                id="username"
                defaultValue="@peduarte"
                className="col-span-3"
              />
            </div>
          </div>
          <SheetFooter>
            <SheetClose asChild>
              <Button type="submit">Save changes</Button>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>
  )
}
```

Sign in to view the code

[Sign in](https://www.shadcn.io/sign-in)

### Reactbutton

```
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...(props as any)}
    />
  )
}

export { Button, buttonVariants }
```

### Reactinput

### Reactlabel

### Reactsheet

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Navigation drawer](https://www.shadcn.io/ui/sheet\#navigation-drawer)

App menu and navigation from the left edge:

Preview

Code

Source

LeftRightTopBottom

```
import { Button } from "@/components/ui/button"
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function SheetSide() {
  return (
    <div
      className="flex justify-center self-start pt-6 w-full"
      style={{
        all: 'revert',
        display: 'flex',
        justifyContent: 'center',
        alignSelf: 'flex-start',
        paddingTop: '1.5rem',
        width: '100%',
        fontSize: '14px',
        lineHeight: '1.5',
        letterSpacing: 'normal'
      }}
    >
      <div className="flex gap-2 flex-wrap justify-center">
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="outline">Left</Button>
          </SheetTrigger>
          <SheetContent side="left">
            <SheetHeader>
              <SheetTitle>Left sidebar</SheetTitle>
              <SheetDescription>
                This sheet slides in from the left side of the screen.
              </SheetDescription>
            </SheetHeader>
            <div className="mt-6 space-y-4">
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                <span>Dashboard</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                <span>Analytics</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                <span>Settings</span>
              </div>
            </div>
          </SheetContent>
        </Sheet>

        <Sheet>
          <SheetTrigger asChild>
            <Button variant="outline">Right</Button>
          </SheetTrigger>
          <SheetContent side="right">
            <SheetHeader>
              <SheetTitle>Right sidebar</SheetTitle>
              <SheetDescription>
                This sheet slides in from the right side.
              </SheetDescription>
            </SheetHeader>
            <div className="mt-6 space-y-3">
              <div className="p-3 bg-muted rounded-lg">
                <h4 className="font-medium">Recent Activity</h4>
                <p className="text-sm text-muted-foreground mt-1">Updated 2 minutes ago</p>
              </div>
              <div className="p-3 bg-muted rounded-lg">
                <h4 className="font-medium">Notifications</h4>
                <p className="text-sm text-muted-foreground mt-1">3 new messages</p>
              </div>
            </div>
          </SheetContent>
        </Sheet>

        <Sheet>
          <SheetTrigger asChild>
            <Button variant="outline">Top</Button>
          </SheetTrigger>
          <SheetContent side="top">
            <SheetHeader>
              <SheetTitle>Top notification</SheetTitle>
              <SheetDescription>
                Perfect for announcements and notifications.
              </SheetDescription>
            </SheetHeader>
            <div className="mt-4 p-4 bg-blue-50 rounded-lg border border-blue-200">
              <p className="text-sm">🎉 Welcome to the new update! Check out our latest features.</p>
            </div>
          </SheetContent>
        </Sheet>

        <Sheet>
          <SheetTrigger asChild>
            <Button variant="outline">Bottom</Button>
          </SheetTrigger>
          <SheetContent side="bottom">
            <SheetHeader>
              <SheetTitle>Bottom sheet</SheetTitle>
              <SheetDescription>
                Great for mobile-style bottom sheets and quick actions.
              </SheetDescription>
            </SheetHeader>
            <div className="grid grid-cols-3 gap-4 mt-6">
              <Button variant="outline" size="sm">Share</Button>
              <Button variant="outline" size="sm">Edit</Button>
              <Button variant="outline" size="sm">Delete</Button>
            </div>
          </SheetContent>
        </Sheet>
      </div>
    </div>
  )
}
```

Sign in to view the code

[Sign in](https://www.shadcn.io/sign-in)

### Reactbutton

```
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...(props as any)}
    />
  )
}

export { Button, buttonVariants }
```

### Reactsheet

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Mobile action sheet](https://www.shadcn.io/ui/sheet\#mobile-action-sheet)

Bottom panels perfect for touch interfaces:

Preview

Code

Source

Add New Project

```
"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function SheetForm() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))
    setIsSubmitting(false)
  }

  return (
    <div
      className="flex justify-center self-start pt-6 w-full"
      style={{
        all: 'revert',
        display: 'flex',
        justifyContent: 'center',
        alignSelf: 'flex-start',
        paddingTop: '1.5rem',
        width: '100%',
        fontSize: '14px',
        lineHeight: '1.5',
        letterSpacing: 'normal'
      }}
    >
      <Sheet>
        <SheetTrigger asChild>
          <Button>Add New Project</Button>
        </SheetTrigger>
        <SheetContent className="w-[400px] sm:w-[540px]">
          <SheetHeader>
            <SheetTitle>Create new project</SheetTitle>
            <SheetDescription>
              Set up your project details. Click save when you're ready to get started.
            </SheetDescription>
          </SheetHeader>
          <form onSubmit={handleSubmit} className="space-y-6 py-6">
            <div className="space-y-2">
              <Label htmlFor="project-name">Project name</Label>
              <Input
                id="project-name"
                placeholder="My awesome project"
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="description">Description</Label>
              <Textarea
                id="description"
                placeholder="Tell us what this project is about..."
                rows={3}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="framework">Framework</Label>
              <Select required>
                <SelectTrigger>
                  <SelectValue placeholder="Select a framework" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="next">Next.js</SelectItem>
                  <SelectItem value="react">React</SelectItem>
                  <SelectItem value="vue">Vue.js</SelectItem>
                  <SelectItem value="svelte">Svelte</SelectItem>
                  <SelectItem value="astro">Astro</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="visibility">Visibility</Label>
                <Select defaultValue="private">
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="public">🌍 Public</SelectItem>
                    <SelectItem value="private">🔒 Private</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label htmlFor="template">Template</Label>
                <Select defaultValue="blank">
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="blank">Blank</SelectItem>
                    <SelectItem value="blog">Blog</SelectItem>
                    <SelectItem value="ecommerce">E-commerce</SelectItem>
                    <SelectItem value="dashboard">Dashboard</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>

            <SheetFooter>
              <SheetClose asChild>
                <Button variant="outline">Cancel</Button>
              </SheetClose>
              <Button type="submit" disabled={isSubmitting}>
                {isSubmitting ? "Creating..." : "Create project"}
              </Button>
            </SheetFooter>
          </form>
        </SheetContent>
      </Sheet>
    </div>
  )
}
```

Sign in to view the code

[Sign in](https://www.shadcn.io/sign-in)

### Reactbutton

```
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...(props as any)}
    />
  )
}

export { Button, buttonVariants }
```

### Reactinput

### Reactlabel

### Reacttextarea

### Reactselect

### Reactsheet

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Filter and search sidebar](https://www.shadcn.io/ui/sheet\#filter-and-search-sidebar)

Contextual controls that don't interrupt browsing:

Preview

Code

Source

Edit Profile

```
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function SheetDemo() {
  return (
    <div
      className="flex justify-center self-start pt-6 w-full"
      style={{
        all: 'revert',
        display: 'flex',
        justifyContent: 'center',
        alignSelf: 'flex-start',
        paddingTop: '1.5rem',
        width: '100%',
        fontSize: '14px',
        lineHeight: '1.5',
        letterSpacing: 'normal'
      }}
    >
      <Sheet>
        <SheetTrigger asChild>
          <Button variant="outline">Edit Profile</Button>
        </SheetTrigger>
        <SheetContent>
          <SheetHeader>
            <SheetTitle>Edit profile</SheetTitle>
            <SheetDescription>
              Make changes to your profile here. Click save when you're done.
            </SheetDescription>
          </SheetHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                Name
              </Label>
              <Input
                id="name"
                defaultValue="Pedro Duarte"
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="username" className="text-right">
                Username
              </Label>
              <Input
                id="username"
                defaultValue="@peduarte"
                className="col-span-3"
              />
            </div>
          </div>
          <SheetFooter>
            <SheetClose asChild>
              <Button type="submit">Save changes</Button>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>
  )
}
```

Sign in to view the code

[Sign in](https://www.shadcn.io/sign-in)

### Reactbutton

```
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...(props as any)}
    />
  )
}

export { Button, buttonVariants }
```

### Reactinput

### Reactlabel

### Reactsheet

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Notification and alert bar](https://www.shadcn.io/ui/sheet\#notification-and-alert-bar)

Top-sliding panels for system messages:

Preview

Code

Source

Edit Profile

```
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function SheetDemo() {
  return (
    <div
      className="flex justify-center self-start pt-6 w-full"
      style={{
        all: 'revert',
        display: 'flex',
        justifyContent: 'center',
        alignSelf: 'flex-start',
        paddingTop: '1.5rem',
        width: '100%',
        fontSize: '14px',
        lineHeight: '1.5',
        letterSpacing: 'normal'
      }}
    >
      <Sheet>
        <SheetTrigger asChild>
          <Button variant="outline">Edit Profile</Button>
        </SheetTrigger>
        <SheetContent>
          <SheetHeader>
            <SheetTitle>Edit profile</SheetTitle>
            <SheetDescription>
              Make changes to your profile here. Click save when you're done.
            </SheetDescription>
          </SheetHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                Name
              </Label>
              <Input
                id="name"
                defaultValue="Pedro Duarte"
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="username" className="text-right">
                Username
              </Label>
              <Input
                id="username"
                defaultValue="@peduarte"
                className="col-span-3"
              />
            </div>
          </div>
          <SheetFooter>
            <SheetClose asChild>
              <Button type="submit">Save changes</Button>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>
  )
}
```

Sign in to view the code

[Sign in](https://www.shadcn.io/sign-in)

### Reactbutton

```
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        outline:
          "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost:
          "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2 has-[>svg]:px-3",
        sm: "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
        lg: "h-10 rounded-md px-6 has-[>svg]:px-4",
        icon: "size-9",
        "icon-sm": "size-8",
        "icon-lg": "size-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...(props as any)}
    />
  )
}

export { Button, buttonVariants }
```

### Reactinput

### Reactlabel

### Reactsheet

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

## [Features](https://www.shadcn.io/ui/sheet\#features)

This free open source sheet component includes everything you need:

- **TypeScript-first** \- Full type safety with sheet state and animation events
- **Radix UI Dialog powered** \- Battle-tested focus management and accessibility
- **Edge positioning** \- Slides from top, right, bottom, or left screen edges
- **Tailwind CSS styled** \- Customize with utilities, not fighting animation CSS
- **Focus trapping** \- Keyboard navigation stays properly contained within sheets
- **Mobile optimized** \- Native app feel with smooth slide animations
- **Contextual overlay** \- Keeps main content visible while showing secondary UI
- **Portal rendering** \- No z-index conflicts or positioning issues

## [API Reference](https://www.shadcn.io/ui/sheet\#api-reference)

### [Core Components](https://www.shadcn.io/ui/sheet\#core-components)

| Component | Purpose | Key Props |
| --- | --- | --- |
| `Sheet` | Root container | `open`, `onOpenChange`, `modal` for behavior |
| `SheetTrigger` | Opens the sheet | `asChild` for custom trigger elements |
| `SheetContent` | Sliding panel | `side` for edge positioning |

### [Content Structure](https://www.shadcn.io/ui/sheet\#content-structure)

| Component | Use Case | Purpose |
| --- | --- | --- |
| `SheetHeader` | Title area | Contains title and description |
| `SheetTitle` | Accessible heading | Screen reader announcements |
| `SheetFooter` | Action buttons | Save, cancel, and primary actions |
| `SheetClose` | Close trigger | Custom close buttons and links |

### [Edge Positioning](https://www.shadcn.io/ui/sheet\#edge-positioning)

| Side | Best For | Use Case |
| --- | --- | --- |
| `"right"` | Settings, details | Desktop sidebars, configuration |
| `"left"` | Navigation, menus | App navigation, drawer menus |
| `"bottom"` | Actions, forms | Mobile interfaces, action sheets |
| `"top"` | Notifications, alerts | System messages, announcements |

## [Production tips](https://www.shadcn.io/ui/sheet\#production-tips)

**Size sheets appropriately for their content and context.** This free shadcn/ui sheet component adapts to any width and height, but overwhelming sheets defeat the purpose. This TypeScript component handles the positioning—you provide dimensions that enhance workflow rather than dominating the screen in your Next.js applications.

**Consider mobile-first design patterns for better touch experiences.** Bottom sheets work naturally on mobile, while side sheets excel on desktop. This open source shadcn sheet supports all edge positions—choose based on your users' devices and interaction patterns rather than just following desktop conventions.

**Keep sheet content contextual and focused.** Sheets work best when they complement what users are already doing, not replace the entire interface. This JavaScript component provides the container—you provide content that enhances the current task without creating workflow disruption.

**Handle long content gracefully with proper scrolling.** When sheet content exceeds viewport height, users need smooth scrolling that doesn't break the slide animation. The Tailwind CSS styled component supports scroll areas—combine with proper content organization to maintain usability.

**Test keyboard navigation thoroughly across all sheet sides.** Focus management works differently when sheets slide from different edges. This component traps focus automatically—ensure your content order makes sense for keyboard users regardless of slide direction and animation timing.

## [Integration with other components](https://www.shadcn.io/ui/sheet\#integration-with-other-components)

Sheets naturally work with [Form](https://www.shadcn.io/ui/form) components for settings and configuration panels in your React applications. Use [Button](https://www.shadcn.io/ui/button) components for consistent trigger styling and sheet action buttons.

For navigation patterns, combine sheets with [NavigationMenu](https://www.shadcn.io/ui/navigation-menu) components for mobile menu drawers or [Breadcrumb](https://www.shadcn.io/ui/breadcrumb) components for contextual navigation. This open source pattern creates comprehensive mobile-first navigation experiences.

When building data-heavy interfaces, pair sheets with [DataTable](https://www.shadcn.io/ui/data-table) components for filter panels or [Command](https://www.shadcn.io/ui/command) components for searchable content. [ScrollArea](https://www.shadcn.io/ui/scroll-area) components handle long sheet content without breaking animations.

For notification systems, use sheets with [Alert](https://www.shadcn.io/ui/alert) components for system messages or [Badge](https://www.shadcn.io/ui/badge) components for status indicators. Your JavaScript application can compose these shadcn components while maintaining consistent slide behavior and focus management across different sheet types.

## [Questions you might have](https://www.shadcn.io/ui/sheet\#questions-you-might-have)

### When should I use Sheet vs Dialog components?

### How do sheets work on mobile devices?

### How does focus management work in sheets?

### Which edge should I choose for different content types?

### Can I customize sheet appearance and animations?

### Are sheets accessible to screen readers?

### Do sheets impact application performance?

### Can I nest sheets or use multiple sheets simultaneously?

[Shadcn Separator\\
\\
React separator for visual content dividers and section breaks with horizontal and vertical orientations. Built with TypeScript and Tailwind CSS for Next.js using Radix UI.](https://www.shadcn.io/ui/separator) [Shadcn Skeleton\\
\\
React skeleton for loading placeholders and shimmer effects that improve perceived performance. Built with TypeScript and Tailwind CSS for Next.js.](https://www.shadcn.io/ui/skeleton)
