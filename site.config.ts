export const config = {
  siteMeta: {
    title: "cistLT Blog Hub",
    teamName: "cistLT club.",
    description:
      "バイオ系、電子工学系、情報工学系と、様々なことに興味があるメンバーがアウトプットとして書いたブログをまとめたサイトです。",
  },
  siteRoot:
    process.env.NODE_ENV === "production"
      ? "https://cistlt-blog-hub.vercel.app"
      : "http://localhost:3000",
  headerLinks: [
    {
      title: "About",
      href: "https://cist-lt-group.web.app/",
    },
    {
      title: "Twitter",
      href: "https://twitter.com/cistLT",
    },
    {
      title: "GitHub",
      href: "https://github.com/cistLT-Club",
    },
  ],
};
