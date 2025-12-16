# Shadcn Sonner

React toast for non-blocking notifications and user feedback with smooth animations. Built with TypeScript and Tailwind CSS for Next.js.

Table of Contents

You know those little notifications that pop up to tell you something worked? Or when you need to undo an action? Ever notice how the best apps make these feel polished instead of jarring interruptions? This shadcn/ui sonner makes toast notifications feel thoughtful and professional in your React applications.

### [Sonner showcase](https://www.shadcn.io/ui/sonner\#sonner-showcase)

Clean, simple toast messages:

Preview

Code

Source

Show Toast

```
"use client"

import { toast } from "sonner"
import { Button } from "@/components/ui/button"

export default function SonnerDemo() {
  return (
    <Button
      variant="outline"
      onClick={() =>
        toast("Event has been created", {
          description: "Sunday, December 03, 2023 at 9:00 AM",
          action: {
            label: "Undo",
            onClick: () => console.log("Undo"),
          },
          classNames: {
            description: "!text-foreground/80",
          },
        })
      }
    >
      Show Toast
    </Button>
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

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

Just import and call `toast()` anywhere in your app. This free open source component handles positioning, animations, and accessibility so your notifications enhance user experience instead of disrupting workflow. Styled with Tailwind CSS to match your design system instead of generic browser alerts.

```
npx shadcn@latest add sonner
```

## [Why sonner actually beats basic alerts](https://www.shadcn.io/ui/sonner\#why-sonner-actually-beats-basic-alerts)

Here's the thing—most notification systems are terrible because they interrupt users at the worst possible moments. Think about those modal alerts that stop everything you're doing just to say "Success!" or browser notifications that cover important interface elements. Good toast notifications appear when they're relevant and disappear gracefully.

Sonner lets users keep working while showing contextual feedback. Need to confirm a file upload? Show progress and success without blocking the interface. Made a mistake? Offer instant undo actions right in the notification. Users get the feedback they need without losing focus or momentum.

This free shadcn sonner handles the complex parts—smart positioning, smooth animations, keyboard accessibility, mobile gestures—while you focus on providing meaningful feedback at the right moments. Whether you're building form confirmations, progress indicators, or undo systems in your Next.js applications, notifications that enhance workflow keep users productive in your JavaScript projects.

## [Common sonner patterns you'll actually use](https://www.shadcn.io/ui/sonner\#common-sonner-patterns-youll-actually-use)

### [Success and error messages](https://www.shadcn.io/ui/sonner\#success-and-error-messages)

Different message types with appropriate styling:

Preview

Code

Source

DefaultSuccessErrorLoading

```
"use client"

import { toast } from "sonner"
import { Button } from "@/components/ui/button"

export default function SonnerTypes() {
  return (
    <div className="flex flex-wrap gap-3">
      <Button
        variant="outline"
        onClick={() => toast("Simple notification", {
          className: "bg-card text-card-foreground border-border"
        })}
      >
        Default
      </Button>
      <Button
        variant="outline"
        onClick={() => toast.success("Upload completed successfully", {
          className: "bg-card text-card-foreground border-border"
        })}
      >
        Success
      </Button>
      <Button
        variant="outline"
        onClick={() => toast.error("Failed to delete item", {
          className: "bg-card text-card-foreground border-border"
        })}
      >
        Error
      </Button>
      <Button
        variant="outline"
        onClick={() => toast.loading("Processing your request...", {
          className: "bg-card text-card-foreground border-border"
        })}
      >
        Loading
      </Button>
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

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Promise and loading states](https://www.shadcn.io/ui/sonner\#promise-and-loading-states)

Automatic progress feedback for async operations:

Preview

Code

Source

Upload File

```
"use client"

import { toast } from "sonner"
import { Button } from "@/components/ui/button"

export default function SonnerPromise() {
  const simulateUpload = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.5) {
          resolve({ name: "document.pdf", size: "2.4MB" })
        } else {
          reject(new Error("Network error"))
        }
      }, 2000)
    })
  }

  const handleUpload = () => {
    const promise = simulateUpload()

    toast.promise(promise, {
      loading: "Uploading file...",
      success: (data: any) => `${data.name} uploaded (${data.size})`,
      error: "Upload failed. Please try again.",
      className: "bg-card text-card-foreground border-border",
    })
  }

  return (
    <Button variant="outline" onClick={handleUpload}>
      Upload File
    </Button>
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

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Custom notification content](https://www.shadcn.io/ui/sonner\#custom-notification-content)

Rich notifications with icons and custom JSX:

Preview

Code

Source

With IconPersistentCustom JSX

```
"use client"

import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Mail, Bell, Heart } from "lucide-react"

export default function SonnerCustom() {
  return (
    <div className="flex flex-wrap gap-3">
      <Button
        variant="outline"
        onClick={() =>
          toast("New message received", {
            description: "From John Doe - 2 minutes ago",
            icon: <Mail className="h-4 w-4" />,
            duration: 5000,
            classNames: {
              description: "!text-foreground/80",
            },
          })
        }
      >
        With Icon
      </Button>

      <Button
        variant="outline"
        onClick={() => {
          const toastId = toast("Settings saved", {
            description: "Your preferences have been updated",
            duration: Infinity,
            action: {
              label: "Dismiss",
              onClick: () => toast.dismiss(toastId),
            },
            className: "bg-card text-card-foreground border-border [&>[data-description]]:text-card-foreground/80",
          })
        }}
      >
        Persistent
      </Button>

      <Button
        variant="outline"
        onClick={() =>
          toast.custom((t) => (
            <div className="bg-gradient-to-r from-pink-500 to-violet-500 text-white p-4 rounded-lg shadow-lg">
              <div className="flex items-center gap-2">
                <Heart className="h-5 w-5" />
                <div>
                  <div className="font-semibold">Custom Toast</div>
                  <div className="text-sm opacity-90">Built with your own JSX</div>
                </div>
                <button
                  onClick={() => toast.dismiss(t)}
                  className="ml-auto bg-white/20 hover:bg-white/30 rounded px-2 py-1 text-xs"
                >
                  Close
                </button>
              </div>
            </div>
          ))
        }
      >
        Custom JSX
      </Button>
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

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Undo and action notifications](https://www.shadcn.io/ui/sonner\#undo-and-action-notifications)

Let users reverse actions immediately:

Preview

Code

Source

Show Toast

```
"use client"

import { toast } from "sonner"
import { Button } from "@/components/ui/button"

export default function SonnerDemo() {
  return (
    <Button
      variant="outline"
      onClick={() =>
        toast("Event has been created", {
          description: "Sunday, December 03, 2023 at 9:00 AM",
          action: {
            label: "Undo",
            onClick: () => console.log("Undo"),
          },
          classNames: {
            description: "!text-foreground/80",
          },
        })
      }
    >
      Show Toast
    </Button>
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

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

### [Persistent system messages](https://www.shadcn.io/ui/sonner\#persistent-system-messages)

Important notifications that stay until dismissed:

Preview

Code

Source

Show Toast

```
"use client"

import { toast } from "sonner"
import { Button } from "@/components/ui/button"

export default function SonnerDemo() {
  return (
    <Button
      variant="outline"
      onClick={() =>
        toast("Event has been created", {
          description: "Sunday, December 03, 2023 at 9:00 AM",
          action: {
            label: "Undo",
            onClick: () => console.log("Undo"),
          },
          classNames: {
            description: "!text-foreground/80",
          },
        })
      }
    >
      Show Toast
    </Button>
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

Sign in to view the source

[Sign in](https://www.shadcn.io/sign-in)

## [Features](https://www.shadcn.io/ui/sonner\#features)

This free open source toast component includes everything you need:

- **TypeScript-first** \- Full type safety with notification events and state management
- **Emil Kowalski created** \- Built by the creator of the original Sonner library
- **Non-blocking interface** \- Users continue working while notifications provide feedback
- **Tailwind CSS styled** \- Customize with utilities, not fighting notification positioning
- **Promise integration** \- Automatic loading, success, and error states for async operations
- **Mobile optimized** \- Swipe to dismiss with touch-friendly interactions
- **Accessibility ready** \- Screen reader announcements and keyboard navigation
- **Smart positioning** \- Never covers critical interface elements or user content

## [API Reference](https://www.shadcn.io/ui/sonner\#api-reference)

### [Core Functions](https://www.shadcn.io/ui/sonner\#core-functions)

| Function | Purpose | Use Case |
| --- | --- | --- |
| `toast(message)` | Basic notification | Simple confirmations and feedback |
| `toast.success(message)` | Success notification | Completed actions, saved changes |
| `toast.error(message)` | Error notification | Failed operations, validation errors |
| `toast.loading(message)` | Loading notification | In-progress operations |
| `toast.promise(promise, options)` | Promise handling | Automatic async operation feedback |

### [Configuration Options](https://www.shadcn.io/ui/sonner\#configuration-options)

| Option | Type | Purpose |
| --- | --- | --- |
| `description` | string | Additional context below main message |
| `duration` | number | Auto-dismiss timing (4000ms default) |
| `action` | object | Primary button with label and onClick |
| `icon` | ReactNode | Custom icon for notification |
| `position` | string | Override default toast position |

### [Toaster Setup](https://www.shadcn.io/ui/sonner\#toaster-setup)

| Component | Purpose | Key Props |
| --- | --- | --- |
| `<Toaster />` | Container for all toasts | `position`, `theme`, `visibleToasts` |

## [Production tips](https://www.shadcn.io/ui/sonner\#production-tips)

**Be specific with notification messages instead of generic feedback.** This free shadcn/ui sonner component shows whatever text you provide—"File uploaded successfully" tells users more than "Success!" This TypeScript component handles the display—you provide messages that actually inform users about what happened in your Next.js applications.

**Use promise integration for async operations and loading states.** When users submit forms or upload files, they need progress feedback. This open source shadcn sonner automatically handles loading, success, and error states—provide clear messaging for each stage of the operation.

**Enable undo actions for destructive operations immediately.** Deleted something important? Let users reverse it right in the notification before it disappears. This JavaScript component supports action buttons—use them to provide safety nets for user mistakes and accidental actions.

**Don't overwhelm users with notification spam.** Too many toasts create noise that users learn to ignore. The Tailwind CSS styled component limits visible notifications automatically—be selective about what deserves user attention and when notifications actually help.

**Position notifications thoughtfully based on your interface layout.** Bottom-right works for most apps, but consider your user's workflow and screen real estate. This component supports any position—choose placement that complements your interface instead of fighting for attention.

## [Integration with other components](https://www.shadcn.io/ui/sonner\#integration-with-other-components)

Sonner naturally works with [Form](https://www.shadcn.io/ui/form) components for validation feedback and submission confirmations in your React applications. Use [Button](https://www.shadcn.io/ui/button) components to trigger toast notifications for user actions and confirmations.

For complex workflows, combine sonner with [Dialog](https://www.shadcn.io/ui/dialog) components—use toasts for quick feedback, dialogs for complex confirmations. This open source pattern provides appropriate feedback levels for different interaction types.

When building data interfaces, pair sonner with [DataTable](https://www.shadcn.io/ui/data-table) components for bulk operation feedback or [Progress](https://www.shadcn.io/ui/progress) components for file upload status. [Alert](https://www.shadcn.io/ui/alert) components work alongside toasts for persistent warnings versus temporary notifications.

For user account features, use sonner with [Avatar](https://www.shadcn.io/ui/avatar) components for profile update confirmations or [Badge](https://www.shadcn.io/ui/badge) components for status change notifications. Your JavaScript application can compose these shadcn components while maintaining consistent feedback patterns across different user interactions.

## [Questions you might have](https://www.shadcn.io/ui/sonner\#questions-you-might-have)

### When should I use Sonner vs Alert components?

### How do I set up Sonner in my Next.js application?

### How does promise integration work with async operations?

### How do toast notifications work on mobile devices?

### Are toast notifications accessible to screen readers?

### Can I customize where notifications appear on screen?

### How do I customize toast appearance and animations?

### How do I implement undo functionality in notifications?

[Shadcn Slider\\
\\
React slider for interactive range inputs and value selectors with drag controls. Built with TypeScript and Tailwind CSS for Next.js using Radix UI.](https://www.shadcn.io/ui/slider) [Shadcn Switch\\
\\
React switch for toggle settings and preferences with smooth animations. Built with TypeScript and Tailwind CSS for Next.js using Radix UI.](https://www.shadcn.io/ui/switch)
