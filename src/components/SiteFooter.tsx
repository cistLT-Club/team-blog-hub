import { ContentWrapper } from "@src/components/ContentWrapper";
import { config } from "@site.config";
import Link from "next/link";

export const SiteFooter: React.FC = () => (
  <>
    <div className="footer">
      <Link href="/" passHref>
        <img src="/logo.name.svg" alt={config.siteMeta.title} />
      </Link>
      <small>©️ {config.siteMeta.teamName}</small>
    </div>
  </>
);
