package net.armagomen.battleobserver.battle.components
{
	import net.armagomen.battleobserver.battle.base.ObserverBattleDispalaysble;
	import net.armagomen.battleobserver.utils.Filters;
	import net.armagomen.battleobserver.utils.TextExt;
	
	public class DistanceUI extends ObserverBattleDispalaysble
	{
		private var distance:TextExt;
		
		public function DistanceUI()
		{
			super();
		}
		
		override protected function onPopulate():void 
		{
			super.onPopulate();
			if (this.distance == null)
			{
				var settings:Object = this.getSettings();
				this.distance = new TextExt(settings.x, settings.y, Filters.middleText, settings.align, this.getShadowSettings(), this);
			}
		}
		
		public function as_setDistance(text:String):void
		{
			this.distance.htmlText = text;
		}
	}
}